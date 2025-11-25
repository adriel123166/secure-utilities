import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from src.utils.util_shortener import shorten_url
from src.utils.sms_messaging import send_message
from src.utils.fake_data_generator import generate_fake_users
from src.widgets.calculator import Calculator


class AccessibleDashboard:
    def __init__(self, parent_root: tk.Tk, username: str):
        self.root = parent_root
        self.username = username

        # Premium dark theme with refined colors
        self.colors = {
            'primary': '#0a0a0a',        # deep black
            'primary_light': '#1a1a1a',  # lighter black
            'accent': '#FFD700',         # gold
            'accent_hover': '#FFC700',   # bright gold
            'accent_dark': '#B8860B',    # dark goldenrod
            'success': '#00D9A3',        # modern teal green
            'success_hover': '#00C794',  # darker teal
            'danger': '#FF4757',         # modern red
            'danger_hover': '#EE3344',   # darker red
            'warning': '#FFA502',        # orange
            'bg_main': '#0d0d0d',        # main background
            'bg_card': '#1a1a1a',        # card background
            'bg_hover': '#252525',       # hover state
            'text_primary': '#FFFFFF',   # pure white
            'text_secondary': '#B0B0B0', # muted white
            'text_dim': '#808080',       # dim gray
            'border': '#2a2a2a',         # subtle border
            'shadow': '#000000'          # shadow
        }

        self.setup_dashboard()
        self.apply_smooth_transitions()

    def setup_dashboard(self):
        """Create professional dashboard with smooth animations"""
        self.dashboard = tk.Frame(self.root, bg=self.colors['bg_main'])
        self.dashboard.pack(fill="both", expand=True)

        # Configure root window
        self.root.state("zoomed")
        self.root.title(f"Secure Utilities • {self.username}")
        self.root.configure(bg=self.colors['bg_main'])

        # Modern header with shadow effect
        self.create_header()
        
        # Professional notebook styling
        self.setup_notebook_styles()
        
        # Main content area
        self.tab_control = ttk.Notebook(self.dashboard, style='Modern.TNotebook')
        self.tab_control.pack(expand=True, fill="both", padx=15, pady=(0, 15))

        # Setup feature tabs
        self.setup_url_shortener()
        self.setup_calculator()
        self.setup_messaging()
        self.setup_fake_data()

        # Modern footer with logout
        self.create_footer()
        
        # Keyboard shortcuts
        self.setup_keyboard_shortcuts()

    def create_header(self):
        """Create modern header with gradient effect"""
        header_container = tk.Frame(self.dashboard, bg=self.colors['bg_main'])
        header_container.pack(fill="x", pady=(0, 15))

        header = tk.Frame(header_container, bg=self.colors['primary'], height=70)
        header.pack(fill="x", padx=15)
        header.pack_propagate(False)

        # Left side - branding
        left_frame = tk.Frame(header, bg=self.colors['primary'])
        left_frame.pack(side="left", padx=25, pady=15)

        tk.Label(
            left_frame,
            text="⚡ SECURE UTILITIES",
            font=("Segoe UI", 16, "bold"),
            fg=self.colors['accent'],
            bg=self.colors['primary']
        ).pack(anchor="w")

        tk.Label(
            left_frame,
            text=f"Welcome back, {self.username}",
            font=("Segoe UI", 9),
            fg=self.colors['text_secondary'],
            bg=self.colors['primary']
        ).pack(anchor="w")

        # Right side - info
        right_frame = tk.Frame(header, bg=self.colors['primary'])
        right_frame.pack(side="right", padx=25, pady=15)

        from datetime import datetime
        tk.Label(
            right_frame,
            text=datetime.now().strftime("%B %d, %Y"),
            font=("Segoe UI", 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['primary']
        ).pack(anchor="e")

        tk.Label(
            right_frame,
            text=datetime.now().strftime("%I:%M %p"),
            font=("Segoe UI", 9),
            fg=self.colors['text_dim'],
            bg=self.colors['primary']
        ).pack(anchor="e")

        # Shadow effect
        shadow = tk.Frame(header_container, bg=self.colors['border'], height=1)
        shadow.pack(fill="x", padx=15)

    def setup_notebook_styles(self):
        """Configure modern notebook styling"""
        style = ttk.Style()
        style.theme_use('clam')

        # Notebook
        style.configure(
            'Modern.TNotebook',
            background=self.colors['bg_main'],
            borderwidth=0,
            tabmargins=[2, 5, 2, 0]
        )

        # Tabs
        style.configure(
            'Modern.TNotebook.Tab',
            background=self.colors['bg_card'],
            foreground=self.colors['text_secondary'],
            padding=[20, 10],
            borderwidth=0,
            font=('Segoe UI', 10, 'normal')
        )

        style.map(
            'Modern.TNotebook.Tab',
            background=[
                ('selected', self.colors['primary_light']),
                ('active', self.colors['bg_hover'])
            ],
            foreground=[
                ('selected', self.colors['accent']),
                ('active', self.colors['text_primary'])
            ],
            font=[('selected', ('Segoe UI', 10, 'bold'))]
        )

    def create_modern_card(self, parent, title, subtitle=None):
        """Create a modern card container"""
        # Main card frame
        card = tk.Frame(parent, bg=self.colors['bg_card'], relief="flat")
        card.pack(fill="both", expand=True, padx=25, pady=25)

        # Card header
        header = tk.Frame(card, bg=self.colors['bg_card'])
        header.pack(fill="x", padx=30, pady=(25, 10))

        tk.Label(
            header,
            text=title,
            font=("Segoe UI", 16, "bold"),
            fg=self.colors['accent'],
            bg=self.colors['bg_card']
        ).pack(anchor="w")

        if subtitle:
            tk.Label(
                header,
                text=subtitle,
                font=("Segoe UI", 9),
                fg=self.colors['text_dim'],
                bg=self.colors['bg_card']
            ).pack(anchor="w", pady=(2, 0))

        # Card content area
        content = tk.Frame(card, bg=self.colors['bg_card'])
        content.pack(fill="both", expand=True, padx=30, pady=(10, 25))

        return card, content

    def create_modern_button(self, parent, text, command, style='primary', icon=None):
        """Create a modern button with hover effects"""
        colors = {
            'primary': (self.colors['accent'], self.colors['accent_hover'], 'black'),
            'success': (self.colors['success'], self.colors['success_hover'], 'white'),
            'danger': (self.colors['danger'], self.colors['danger_hover'], 'white')
        }

        bg, hover_bg, fg = colors.get(style, colors['primary'])

        if icon:
            text = f"{icon}  {text}"

        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=bg,
            fg=fg,
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=12,
            command=command,
            borderwidth=0
        )

        # Smooth hover effect
        def on_enter(e):
            btn.config(bg=hover_bg)

        def on_leave(e):
            btn.config(bg=bg)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    def create_modern_entry(self, parent, placeholder="", width=None):
        """Create a modern input field"""
        entry = tk.Entry(
            parent,
            font=("Segoe UI", 11),
            bg=self.colors['primary_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['accent'],
            relief="flat",
            bd=0
        )

        if width:
            entry.config(width=width)

        # Add placeholder behavior
        if placeholder:
            entry.insert(0, placeholder)
            entry.config(fg=self.colors['text_dim'])

            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, tk.END)
                    entry.config(fg=self.colors['text_primary'])

            def on_focus_out(event):
                if not entry.get():
                    entry.insert(0, placeholder)
                    entry.config(fg=self.colors['text_dim'])

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)

        return entry

    # ==== URL SHORTENER ====
    def setup_url_shortener(self):
        tab = tk.Frame(self.tab_control, bg=self.colors['bg_main'])
        self.tab_control.add(tab, text="  🔗  URL Shortener  ")

        card, content = self.create_modern_card(
            tab,
            "URL Shortener",
            "Shorten long URLs into compact, shareable links"
        )

        # Input field
        self.url_entry = self.create_modern_entry(content, "https://example.com/very/long/url")
        self.url_entry.pack(fill="x", ipady=12, pady=(10, 20))

        # Result label
        self.url_result = tk.Label(
            content,
            text="",
            font=("Segoe UI", 10),
            bg=self.colors['bg_card'],
            fg=self.colors['text_secondary'],
            wraplength=600,
            justify="left"
        )
        self.url_result.pack(fill="x", pady=(0, 20))

        # Action button
        self.create_modern_button(
            content,
            "Shorten URL",
            self.do_shorten,
            style='primary',
            icon="✨"
        ).pack()

    # ==== CALCULATOR ====
    def setup_calculator(self):
        tab = tk.Frame(self.tab_control, bg=self.colors['bg_main'])
        self.tab_control.add(tab, text="  🔢  Calculator  ")

        card, content = self.create_modern_card(
            tab,
            "Advanced Calculator",
            "Perform complex calculations with ease"
        )

        # Calculator icon
        icon_label = tk.Label(
            content,
            text="🔢",
            font=("Segoe UI", 60),
            bg=self.colors['bg_card'],
            fg=self.colors['accent']
        )
        icon_label.pack(pady=(30, 20))

        # Description
        tk.Label(
            content,
            text="Launch the calculator to perform mathematical operations",
            font=("Segoe UI", 10),
            bg=self.colors['bg_card'],
            fg=self.colors['text_secondary']
        ).pack(pady=(0, 30))

        # Launch button
        self.create_modern_button(
            content,
            "Launch Calculator",
            self.open_calculator,
            style='success',
            icon="🚀"
        ).pack()

    # ==== MESSAGING ====
    def setup_messaging(self):
        tab = tk.Frame(self.tab_control, bg=self.colors['bg_main'])
        self.tab_control.add(tab, text="  💬  Messaging  ")

        card, content = self.create_modern_card(
            tab,
            "Send Message",
            "Send SMS messages to any phone number"
        )

        # Recipient field
        tk.Label(
            content,
            text="Recipient Phone Number",
            font=("Segoe UI", 9, "bold"),
            bg=self.colors['bg_card'],
            fg=self.colors['text_secondary']
        ).pack(anchor="w", pady=(0, 5))

        self.msg_recipient = self.create_modern_entry(content, "+1 (555) 123-4567")
        self.msg_recipient.pack(fill="x", ipady=12, pady=(0, 20))

        # Message field
        tk.Label(
            content,
            text="Message",
            font=("Segoe UI", 9, "bold"),
            bg=self.colors['bg_card'],
            fg=self.colors['text_secondary']
        ).pack(anchor="w", pady=(0, 5))

        text_container = tk.Frame(content, bg=self.colors['primary_light'])
        text_container.pack(fill="both", expand=True, pady=(0, 5))

        self.msg_text = scrolledtext.ScrolledText(
            text_container,
            font=("Segoe UI", 10),
            bg=self.colors['primary_light'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['accent'],
            height=6,
            relief="flat",
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.msg_text.pack(fill="both", expand=True)
        self.msg_text.bind("<KeyRelease>", self.update_char_count)

        # Character counter
        self.char_count = tk.Label(
            content,
            text="0 / 1600 characters",
            font=("Segoe UI", 8),
            fg=self.colors['text_dim'],
            bg=self.colors['bg_card']
        )
        self.char_count.pack(anchor="e", pady=(5, 10))

        # Status label
        self.msg_status = tk.Label(
            content,
            text="",
            font=("Segoe UI", 9),
            bg=self.colors['bg_card'],
            fg=self.colors['success']
        )
        self.msg_status.pack(pady=(0, 20))

        # Send button
        self.create_modern_button(
            content,
            "Send Message",
            self.do_send_message,
            style='success',
            icon="📤"
        ).pack()

    # ==== FAKE DATA ====
    def setup_fake_data(self):
        tab = tk.Frame(self.tab_control, bg=self.colors['bg_main'])
        self.tab_control.add(tab, text="  📊  Fake Data  ")

        card, content = self.create_modern_card(
            tab,
            "Fake Data Generator",
            "Generate realistic fake user data for testing"
        )

        # Control panel
        control_frame = tk.Frame(content, bg=self.colors['bg_card'])
        control_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            control_frame,
            text="Number of records:",
            font=("Segoe UI", 9, "bold"),
            bg=self.colors['bg_card'],
            fg=self.colors['text_secondary']
        ).pack(side="left", padx=(0, 10))

        self.fake_count = self.create_modern_entry(control_frame, width=8)
        self.fake_count.delete(0, tk.END)
        self.fake_count.insert(0, "5")
        self.fake_count.config(fg=self.colors['text_primary'])
        self.fake_count.pack(side="left", ipady=8, padx=(0, 15))

        self.create_modern_button(
            control_frame,
            "Generate",
            self.do_generate_fake,
            style='primary',
            icon="⚡"
        ).pack(side="left")

        # Results area
        results_container = tk.Frame(content, bg=self.colors['primary'])
        results_container.pack(fill="both", expand=True, pady=(0, 0))

        self.fake_results = scrolledtext.ScrolledText(
            results_container,
            font=("Consolas", 9),
            bg=self.colors['primary'],
            fg=self.colors['text_primary'],
            insertbackground=self.colors['accent'],
            height=12,
            relief="flat",
            wrap=tk.WORD,
            padx=15,
            pady=15
        )
        self.fake_results.pack(fill="both", expand=True)
        self.fake_results.insert("1.0", "Click 'Generate' to create fake user data...")
        self.fake_results.config(state="disabled", fg=self.colors['text_dim'])

    def create_footer(self):
        """Create modern footer with logout"""
        footer = tk.Frame(self.dashboard, bg=self.colors['bg_main'])
        footer.pack(fill="x", padx=15, pady=(0, 15))

        # Logout button
        logout_btn = self.create_modern_button(
            footer,
            "Logout",
            self.do_logout,
            style='danger',
            icon="🚪"
        )
        logout_btn.pack(side="right")

    # ==== LOGIC METHODS ====
    def update_char_count(self, event=None):
        """Update character count with color coding"""
        count = len(self.msg_text.get("1.0", "end-1c"))
        max_chars = 1600

        if count > max_chars:
            color = self.colors['danger']
        elif count > max_chars * 0.9:
            color = self.colors['warning']
        else:
            color = self.colors['text_dim']

        self.char_count.config(
            text=f"{count} / {max_chars} characters",
            fg=color
        )

    def do_shorten(self):
        """Handle URL shortening with smooth feedback"""
        url = self.url_entry.get().strip()
        
        # Clear placeholder
        if url == "https://example.com/very/long/url":
            url = ""
        
        if not url:
            self.url_result.config(
                text="⚠️  Please enter a valid URL",
                fg=self.colors['warning']
            )
            return

        try:
            short = shorten_url(url)
            self.url_result.config(
                text=f"✅  Shortened: {short}",
                fg=self.colors['success']
            )
            # Auto-clear after 8 seconds
            self.root.after(8000, lambda: self.url_result.config(text=""))
        except Exception as e:
            self.url_result.config(
                text=f"❌  Error: {str(e)}",
                fg=self.colors['danger']
            )

    def open_calculator(self):
        """Open calculator window"""
        Calculator(self.root)

    def do_send_message(self):
        """Handle message sending"""
        recipient = self.msg_recipient.get().strip()
        message = self.msg_text.get("1.0", "end-1c").strip()

        # Clear placeholder
        if recipient == "+1 (555) 123-4567":
            recipient = ""

        if not recipient or not message:
            self.msg_status.config(
                text="⚠️  Please fill in all fields",
                fg=self.colors['warning']
            )
            return

        result = send_message(recipient, message)

        if result.success:
            self.msg_status.config(
                text=f"✅  {result.message}",
                fg=self.colors['success']
            )
            # Clear after success
            self.root.after(3000, lambda: [
                self.msg_recipient.delete(0, tk.END),
                self.msg_text.delete("1.0", tk.END),
                self.msg_status.config(text=""),
                self.char_count.config(text="0 / 1600 characters", fg=self.colors['text_dim'])
            ])
        else:
            self.msg_status.config(
                text=f"❌  {result.message}",
                fg=self.colors['danger']
            )

    def do_generate_fake(self):
        """Generate fake user data"""
        try:
            count = int(self.fake_count.get())
            
            if count < 1 or count > 100:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100")
                return

            users = generate_fake_users(count)

            self.fake_results.config(state="normal", fg=self.colors['text_primary'])
            self.fake_results.delete("1.0", "end")

            for i, user in enumerate(users, 1):
                self.fake_results.insert("end",
                    f"{'═' * 70}\n"
                    f"  USER #{i:02d}\n"
                    f"{'═' * 70}\n"
                    f"  Name:     {user['name']}\n"
                    f"  Email:    {user['email']}\n"
                    f"  Phone:    {user['phone']}\n"
                    f"  Address:  {user['address']}\n\n"
                )

            self.fake_results.config(state="disabled")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def do_logout(self):
        """Handle logout with confirmation"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            # Fade out animation
            self.fade_out()
            self.root.after(300, self.complete_logout)

    def complete_logout(self):
        """Complete the logout process"""
        self.dashboard.destroy()
        self.root.state("normal")
        self.root.geometry("420x380")
        self.root.attributes('-alpha', 1.0)
        from main import setup_login_ui
        setup_login_ui(self.root)

    def setup_keyboard_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.root.bind("<Alt-s>", lambda e: self.do_shorten())
        self.root.bind("<Alt-c>", lambda e: self.open_calculator())
        self.root.bind("<Alt-m>", lambda e: self.do_send_message())
        self.root.bind("<Alt-g>", lambda e: self.do_generate_fake())
        self.root.bind("<Alt-l>", lambda e: self.do_logout())
        self.root.bind("<Escape>", lambda e: self.do_logout())

    def apply_smooth_transitions(self):
        """Apply fade-in animation"""
        self.root.attributes('-alpha', 0.0)
        self.fade_in()

    def fade_in(self):
        """Smooth fade-in animation"""
        alpha = self.root.attributes('-alpha')
        if alpha < 1.0:
            alpha = min(1.0, alpha + 0.05)
            self.root.attributes('-alpha', alpha)
            self.root.after(15, self.fade_in)

    def fade_out(self):
        """Smooth fade-out animation"""
        alpha = self.root.attributes('-alpha')
        if alpha > 0.3:
            alpha = max(0.3, alpha - 0.05)
            self.root.attributes('-alpha', alpha)
            self.root.after(15, self.fade_out)


def build_dashboard(parent_root: tk.Tk, username: str):
    """Create and return the dashboard instance"""
    return AccessibleDashboard(parent_root, username)