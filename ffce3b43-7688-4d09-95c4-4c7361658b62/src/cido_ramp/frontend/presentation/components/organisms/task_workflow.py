import flet as ft
from typing import List, Dict, Callable, Any

class TaskWorkflow(ft.Container):
    """
    Ramp Task Workflow Organism.
    Located in: src/cido_ramp/frontend/presentation/components/organisms/task_workflow.py
    
    This component manages the primary content workspace of Ramp workflows:
    - Current Page Breadcrumbs
    - Horizontal Task Progress Timeline
    - Task List (Title Label, list items with status icons and Action buttons)
    - Dynamic Cost Data Sidebar Panel
    - Dynamic Role Based Access Control (RBAC) validations
    
    Colors mapped to Product Visual Guidelines:
    - BG: #ffffff
    - FG: #111111
    - Accent: #1677ff
    - Surface: #f7f8fa
    - Muted: #6b7280
    - Border: #d9dee7
    """
    
    def __init__(
        self,
        workflow_id: str,
        workflow_type: str,  # 'request-estimate', 'request-new', 'edit', 'archive', 'monitor'
        tasks: List[Dict[str, Any]],
        cost_data: Dict[str, str],
        on_task_action: Callable[[str, str], None],  # callback: on_task_action(task_key, action_type)
        role: str = "owner",  # "owner" or "reviewer"
        current_task_key: str = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.workflow_id = workflow_id
        self.workflow_type = workflow_type
        self.tasks = tasks
        self.cost_data = cost_data
        self.on_task_action = on_task_action
        self.role = role
        self.current_task_key = current_task_key or (tasks[0]["key"] if tasks else None)
        
        # Product Brand Tokens mapped to Hex values
        self.color_bg = "#ffffff"
        self.color_fg = "#111111"
        self.color_accent = "#1677ff"
        self.color_surface = "#f7f8fa"
        self.color_muted = "#6b7280"
        self.color_border = "#d9dee7"
        
        self.expand = True
        self.bgcolor = self.color_bg
        self.padding = ft.padding.all(32)
        
        # Resolve workflow titles & labels
        self.workflow_titles = {
            'request-estimate': 'Request Cost Estimate',
            'request-new': 'Request New Environment',
            'edit': 'Edit Environment',
            'archive': 'Archive Environment',
            'monitor': 'Monitor Environments'
        }
        
        self.workflow_list_labels = {
            'request-estimate': 'ABCD ',
            'request-new': "Let's get your environment set up",
            'edit': 'Modify compute resource allocations',
            'archive': 'Execute safe deprovisioning sequence',
            'monitor': 'Review environment status and allocation metrics'
        }
        
        self.workflow_title = self.workflow_titles.get(self.workflow_type, 'Ramp Workflow')
        self.list_label = self.workflow_list_labels.get(self.workflow_type, 'Workflow Task List')
        
        self.build_ui()

    def build_ui(self):
        # 1. Breadcrumbs Row
        breadcrumbs = ft.Row(
            controls=[
                ft.Text("Ramp", size=12, color=self.color_muted, weight=ft.FontWeight.W_500),
                ft.Icon(name=ft.Icons.CHEVRON_RIGHT, size=14, color=self.color_muted),
                ft.Text(self.workflow_title, size=12, color=self.color_muted, weight=ft.FontWeight.W_500),
            ],
            spacing=6,
        )
        
        # If inside a specific sub-task view
        if self.current_task_key:
            active_task = next((t for t in self.tasks if t["key"] == self.current_task_key), None)
            if active_task:
                breadcrumbs.controls.extend([
                    ft.Icon(name=ft.Icons.CHEVRON_RIGHT, size=14, color=self.color_muted),
                    ft.Text(active_task["name"], size=12, color=self.color_fg, weight=ft.FontWeight.W_600)
                ])

        # 2. Main Title Header
        title_header = ft.Column(
            controls=[
                breadcrumbs,
                ft.Text(
                    self.workflow_title,
                    size=24,
                    weight=ft.FontWeight.W_600,
                    color=self.color_fg,
                    font_family="Inter"
                ),
            ],
            spacing=8,
        )

        # 3. Horizontal Task Progress Timeline
        progress_steps = []
        for i, task in enumerate(self.tasks):
            # Resolve task timeline fill state
            status = task.get("status", "Not Started")
            bar_color = self.color_border
            text_color = self.color_muted
            text_weight = ft.FontWeight.W_500
            
            if status == "Completed":
                bar_color = self.color_fg
                text_color = self.color_fg
            elif status == "In Progress" or task["key"] == self.current_task_key:
                bar_color = self.color_accent
                text_color = self.color_fg
                text_weight = ft.FontWeight.W_600
                
            progress_steps.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                height=6,
                                bgcolor=bar_color,
                                border_radius=ft.border_radius.all(3),
                                expand=True
                            ),
                            ft.Text(
                                task["name"],
                                size=11,
                                color=text_color,
                                weight=text_weight,
                                font_family="Inter",
                                overflow=ft.TextOverflow.ELLIPSIS
                            )
                        ],
                        spacing=6,
                    ),
                    expand=True,
                )
            )
            
        progress_timeline = ft.Container(
            content=ft.Row(controls=progress_steps, spacing=12),
            bgcolor=self.color_surface,
            border=ft.border.all(1, self.color_border),
            border_radius=ft.border_radius.all(8),
            padding=ft.padding.symmetric(vertical=16, horizontal=20),
            margin=ft.margin.only(bottom=24)
        )

        # 4. Primary Content Split Layout (Tasks List vs Cost Data Card)
        task_items = []
        for task in self.tasks:
            task_status = task.get("status", "Not Started")
            
            # Action button setup based on status
            action_label = "Start"
            is_accent = False
            if task_status == "Completed":
                action_label = "Edit"
            elif task_status == "In Progress":
                action_label = "Resume"
                is_accent = True
                
            # Render status indicators with Product brand color constraints
            status_color = self.color_muted
            status_icon = ft.Icons.RADIO_BUTTON_UNCHECKED
            if task_status == "Completed":
                status_color = self.color_fg
                status_icon = ft.Icons.CHECK_CIRCLE
            elif task_status == "In Progress":
                status_color = self.color_accent
                status_icon = ft.Icons.PLAY_CIRCLE_FILLED

            # RBAC Enforcement: Disable actions for Reviewer if required
            btn_disabled = False
            if self.role == "reviewer" and self.workflow_type in ['edit', 'archive']:
                btn_disabled = True

            action_button = ft.ElevatedButton(
                text=action_label,
                color=self.color_bg if is_accent else self.color_fg,
                bgcolor=self.color_accent if is_accent else self.color_bg,
                surface_tint_color=ft.Colors.TRANSPARENT,
                elevation=0,
                disabled=btn_disabled,
                on_click=lambda e, tk=task["key"]: self.on_task_action(tk, action_label.lower()),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    border=ft.BorderSide(1, self.color_accent if is_accent else self.color_border)
                )
            )

            task_row = ft.Container(
                content=ft.Row(
                    controls=[
                        # Task Info
                        ft.Column(
                            controls=[
                                ft.Text(task["name"], size=15, weight=ft.FontWeight.W_600, color=self.color_fg),
                                ft.Text(task.get("desc", ""), size=12, color=self.color_muted)
                            ],
                            spacing=4,
                            expand=True
                        ),
                        # Task Actions / Status
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=status_icon, size=14, color=status_color),
                                        ft.Text(task_status.upper(), size=11, weight=ft.FontWeight.W_600, color=status_color, letter_spacing=0.04)
                                    ],
                                    spacing=6
                                ),
                                action_button
                            ],
                            spacing=16
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                bgcolor=self.color_surface,
                border=ft.border.all(1, self.color_border),
                border_radius=ft.border_radius.all(8),
                padding=ft.padding.all(16)
            )
            task_items.append(task_row)

        tasks_list_col = ft.Column(
            controls=[
                ft.Text(self.list_label.upper(), size=12, weight=ft.FontWeight.W_600, color=self.color_muted, letter_spacing=0.05),
                ft.Divider(height=1, color=self.color_border),
                ft.Column(controls=task_items, spacing=12)
            ],
            spacing=16,
            expand=True
        )

        # 5. Cost Data Sidebar Panel Control
        cost_rows = []
        for key, val in self.cost_data.items():
            if key == "monthlyCost":
                continue
            # Label format mapping
            label = key.upper()
            if key == "cpu": label = "CORE ALLOCATION"
            elif key == "ram": label = "MEMORY POOL"
            elif key == "gpu": label = "GPU ACCELERATORS"
            elif key == "nodes": label = "COMPUTE INSTANCES"
            
            cost_rows.append(
                ft.Row(
                    controls=[
                        ft.Text(label, size=11, color=self.color_muted, weight=ft.FontWeight.W_500),
                        ft.Text(val, size=12, color=self.color_fg, weight=ft.FontWeight.W_600, font_family="monospace")
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        monthly_total_box = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("ESTIMATED RATE", size=11, color=self.color_fg, weight=ft.FontWeight.W_600),
                    ft.Text(self.cost_data.get("monthlyCost", "$0.00"), size=15, color=self.color_accent, weight=ft.FontWeight.W_700, font_family="monospace")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            bgcolor=self.color_bg,
            border=ft.border.all(1, self.color_border),
            border_radius=ft.border_radius.all(6),
            padding=ft.padding.all(12),
            margin=ft.margin.only(top=8)
        )

        cost_sidebar = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("ACTIVE COST DATA", size=12, weight=ft.FontWeight.W_600, color=self.color_fg, letter_spacing=0.05),
                    ft.Divider(height=1, color=self.color_border),
                    ft.Column(controls=cost_rows, spacing=10),
                    monthly_total_box
                ],
                spacing=12
            ),
            bgcolor=self.color_surface,
            border=ft.border.all(1, self.color_border),
            border_radius=ft.border_radius.all(8),
            padding=ft.padding.all(20),
            width=320,
            alignment=ft.alignment.top_center
        )

        # Main Layout Rows
        workspace_layout = ft.Row(
            controls=[
                tasks_list_col,
                cost_sidebar
            ],
            spacing=24,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            expand=True
        )

        # Assemble main view with scrollbar
        self.content = ft.Column(
            controls=[
                title_header,
                progress_timeline,
                workspace_layout
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

    def update_states(self, updated_tasks: List[Dict[str, Any]], updated_cost: Dict[str, str]):
        """Helper to dynamically update UI state on parent-driven event loops"""
        self.tasks = updated_tasks
        self.cost_data = updated_cost
        self.build_ui()
        self.update()
