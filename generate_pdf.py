import sys
import os
import html
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def safe_p(text):
    """Escapes XML entities while preserving simple formatting tags"""
    # Replace dangerous raw XML
    text = text.replace('&', '&amp;')
    text = text.replace('<img />', '&lt;img /&gt;')
    text = text.replace('<input />', '&lt;input /&gt;')
    text = text.replace('<br />', '&lt;br /&gt;')
    text = text.replace('<hr />', '&lt;hr /&gt;')
    text = text.replace('<> ... </>', '&lt;&gt; ... &lt;/&gt;')
    text = text.replace('<>...</>', '&lt;&gt;...&lt;/&gt;')
    text = text.replace('<div id="root">', '&lt;div id="root"&gt;')
    text = text.replace('<div id=\'root\'>', '&lt;div id=\'root\'&gt;')
    text = text.replace('<App />', '&lt;App /&gt;')
    text = text.replace('<React.StrictMode>', '&lt;React.StrictMode&gt;')
    text = text.replace('<StudentCard />', '&lt;StudentCard /&gt;')
    text = text.replace('<studentCard />', '&lt;studentCard /&gt;')
    text = text.replace('<ProfileCard />', '&lt;ProfileCard /&gt;')
    text = text.replace('<Header />', '&lt;Header /&gt;')
    text = text.replace('<StudentRow', '&lt;StudentRow')
    text = text.replace('<table', '&lt;table')
    text = text.replace('<tr>', '&lt;tr&gt;')
    text = text.replace('<div>', '&lt;div&gt;')
    text = text.replace('<span>', '&lt;span&gt;')
    text = text.replace('<button>', '&lt;button&gt;')
    text = text.replace('</h1>', '&lt;/h1&gt;')
    text = text.replace('<h1>', '&lt;h1&gt;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    # Restore allowed tags
    text = text.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    text = text.replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')
    text = text.replace('&lt;code&gt;', '<font name="Courier">').replace('&lt;/code&gt;', '</font>')
    text = text.replace('&lt;br/&gt;', '<br/>').replace('&lt;br&gt;', '<br/>')
    return text

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Header on all pages except page 1
        if self._pageNumber > 1:
            self.setFont('Helvetica-Bold', 8)
            self.setFillColor(colors.HexColor('#1e3a8a'))
            self.drawString(40, letter[1] - 28, "MOHAMMED SATHAK INSTITUTIONS")
            self.setFont('Helvetica', 8)
            self.setFillColor(colors.HexColor('#64748b'))
            self.drawRightString(letter[0] - 40, letter[1] - 28, "Day 1: React & JSX Tutor Teaching Script")
            self.setStrokeColor(colors.HexColor('#cbd5e1'))
            self.setLineWidth(0.5)
            self.line(40, letter[1] - 32, letter[0] - 40, letter[1] - 32)

        # Footer on all pages
        self.setStrokeColor(colors.HexColor('#cbd5e1'))
        self.setLineWidth(0.5)
        self.line(40, 34, letter[0] - 40, 34)

        self.setFont('Helvetica', 8)
        self.setFillColor(colors.HexColor('#64748b'))
        self.drawString(40, 22, "React Bootcamp | 6-Hour Masterclass & Execution Manual")
        self.drawRightString(letter[0] - 40, 22, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename="Tutor-Guide-Day-01-React-and-JSX.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1e3a8a'),
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#475569'),
        alignment=TA_CENTER
    )

    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=body_style,
        leftIndent=14,
        firstLineIndent=-9,
        spaceAfter=2.5
    )

    script_style = ParagraphStyle(
        'TutorScript',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#1e3a8a')
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )

    th_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white,
        alignment=TA_LEFT
    )

    td_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#1e293b')
    )

    td_bold = ParagraphStyle(
        'TableCellBold',
        parent=td_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title Block
    story.append(Spacer(1, 6))
    story.append(Paragraph("MOHAMMED SATHAK INSTITUTIONS", ParagraphStyle('Inst', parent=title_style, fontSize=12, leading=14, textColor=colors.HexColor('#2563eb'))))
    story.append(Spacer(1, 4))
    story.append(Paragraph("DAY 1: Introduction to React & JSX", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Complete 6-Hour Tutor Teaching Script & Execution Manual", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1e3a8a'), spaceAfter=10))

    # Meta Table
    meta_data = [
        [Paragraph(safe_p("<b>Target Audience:</b> Engineering & IT Students"), td_style), Paragraph(safe_p("<b>Duration:</b> 6 Hours Hands-On Masterclass"), td_style)],
        [Paragraph(safe_p("<b>Focus:</b> React Fundamentals, SPA, JSX, Components"), td_style), Paragraph(safe_p("<b>Tools:</b> Node.js, npm, Vite, VS Code, Git"), td_style)]
    ]
    meta_table = Table(meta_data, colWidths=[270, 262])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # Section 1: Schedule Breakdown
    story.append(Paragraph("1. Master 6-Hour Schedule Breakdown", h1_style))
    sched_data = [
        [Paragraph("Time Window", th_style), Paragraph("Module / Topic", th_style), Paragraph("Mode", th_style), Paragraph("Deliverable", th_style)],
        [Paragraph("00:00 - 00:30 (30m)", td_bold), Paragraph("01. Introduction to React & SPA", td_style), Paragraph("Interactive Lecture", td_style), Paragraph(safe_p("Understand SPA mechanics & CSR vs SSR"), td_style)],
        [Paragraph("00:30 - 01:00 (30m)", td_bold), Paragraph("02. React vs Traditional Web Dev", td_style), Paragraph("Code Demo", td_style), Paragraph(safe_p("Compare Vanilla DOM vs React Declarative Counter"), td_style)],
        [Paragraph("01:00 - 01:30 (30m)", td_bold), Paragraph("03. Node.js & npm Setup", td_style), Paragraph("Terminal Hands-on", td_style), Paragraph(safe_p("Environment checks & package.json structure"), td_style)],
        [Paragraph("01:30 - 01:50 (20m)", td_bold), Paragraph("04. Vite Project Creation", td_style), Paragraph("Live Scaffold", td_style), Paragraph(safe_p("Scaffold React app with Vite in seconds"), td_style)],
        [Paragraph("01:50 - 02:00 (10m)", td_bold), Paragraph("05. Understanding Project Structure", td_style), Paragraph("Walkthrough", td_style), Paragraph(safe_p("Trace index.html -> main.jsx -> App.jsx"), td_style)],
        [Paragraph("02:00 - 03:00 (60m)", td_bold), Paragraph("06. JSX Syntax & Expressions", td_style), Paragraph("Coding + Lab", td_style), Paragraph(safe_p("Curly braces expressions, fragments, JSX rules"), td_style)],
        [Paragraph("03:00 - 04:00 (60m)", td_bold), Paragraph("07. Functional Components", td_style), Paragraph("Coding + Lab", td_style), Paragraph(safe_p("PascalCase convention, default/named exports"), td_style)],
        [Paragraph("04:00 - 05:00 (60m)", td_bold), Paragraph("08. Component Rendering", td_style), Paragraph("Coding + Lab", td_style), Paragraph(safe_p("List rendering with .map() and mandatory key prop"), td_style)],
        [Paragraph("05:00 - 05:40 (40m)", td_bold), Paragraph("09. Practical: Student Dashboard", td_style), Paragraph("Capstone Project", td_style), Paragraph(safe_p("Build & run modular Student Profile Dashboard"), td_style)],
        [Paragraph("05:40 - 06:00 (20m)", td_bold), Paragraph("10. Placement Focus & Mock Interview", td_style), Paragraph("Rapid-fire Drill", td_style), Paragraph(safe_p("Answer high-frequency fresher interview questions"), td_style)]
    ]
    sched_table = Table(sched_data, colWidths=[90, 150, 90, 202])
    sched_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('PADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    story.append(sched_table)
    story.append(Spacer(1, 10))

    # Helper function for Tutor Callout
    def make_callout(script_text, title="TUTOR SPOKEN SCRIPT (Say this to the class):", bg_color='#eff6ff', border_color='#2563eb'):
        content = [
            Paragraph(f"<b>🎙️ {title}</b>", ParagraphStyle('CalloutHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=colors.HexColor(border_color))),
            Spacer(1, 2),
            Paragraph(f'"{safe_p(script_text)}"', script_style)
        ]
        t = Table([[content]], colWidths=[532])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_color)),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor(border_color)),
            ('PADDING', (0,0), (-1,-1), 5)
        ]))
        return t

    def make_code_box(code_text, label="EXECUTION & TERMINAL COMMANDS:"):
        escaped_lines = [safe_p(line).replace(' ', '&nbsp;') for line in code_text.split('\n')]
        formatted_code = '<br/>'.join(escaped_lines)
        content = [
            Paragraph(f"<b>💻 {label}</b>", ParagraphStyle('CodeHead', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7, leading=9, textColor=colors.HexColor('#0f172a'))),
            Spacer(1, 2),
            Paragraph(formatted_code, code_style)
        ]
        t = Table([[content]], colWidths=[532])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
            ('PADDING', (0,0), (-1,-1), 4)
        ]))
        return t

    # SECTION 2: Topic-by-Topic Guide
    story.append(Paragraph("2. Module-by-Module Teaching Script & Execution Walkthrough", h1_style))

    # Topic 1
    story.append(Paragraph("Module 01: Introduction to React and SPA (Hour 1: 00:00 - 00:30)", h2_style))
    story.append(make_callout(
        "Welcome to Day 1! When you use Gmail or Instagram, does the entire page refresh when you click an email or post? No! The navbar stays put, and only the central content updates. That is a Single Page Application (SPA). Historically, multi-page websites reloaded the entire screen on every click. In 2011, Facebook created React to solve UI sync issues. React is a JavaScript library that builds dynamic UIs using reusable building blocks called components.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("<b>How to Execute & Demonstrate:</b>"), body_style))
    story.append(Paragraph(safe_p("• Open <code>01-introduction-to-react-and-spa/programs/spa-demo-practice.js</code> on projector."), bullet_style))
    story.append(Paragraph(safe_p("• Explain how <code>navigateTo(page)</code> swaps content inside <code>#root</code> without reloading the browser."), bullet_style))
    story.append(Paragraph(safe_p("• Have students open <code>notes/notes.md</code> and write definitions for React, SPA, MPA, and CSR."), bullet_style))
    story.append(Paragraph(safe_p("• Direct students to <code>exercises/exercise-spa-concept.md</code> to add a new 'grades' view."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 2
    story.append(Paragraph("Module 02: React vs Traditional Web Development (Hour 1: 00:30 - 01:00)", h2_style))
    story.append(make_callout(
        "In Vanilla JS, you write imperative code: document.getElementById('count'), listen for clicks, manually change innerText. With 50 buttons, this becomes an unmaintainable mess! Every DOM touch triggers expensive browser Reflow and Repaint. In React, we write declarative code: UI = f(State). You declare what the UI should look like, and React's Virtual DOM compares differences using an O(n) Diffing Algorithm and patches only changed nodes. This is Reconciliation.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("<b>How to Execute & Demonstrate:</b>"), body_style))
    story.append(Paragraph(safe_p("• Open <code>02-react-vs-traditional-web-development/programs/vanilla-counter.html</code> in Chrome. Demonstrate manual DOM querying."), bullet_style))
    story.append(Paragraph(safe_p("• Open <code>programs/react-counter.jsx</code>. Highlight: <i>Notice there is zero document.getElementById! React syncs UI to state automatically.</i>"), bullet_style))
    story.append(Paragraph(safe_p("• Direct students to <code>exercises/exercise-dom-vs-react.jsx</code> to complete the declarative toggle button."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 3
    story.append(Paragraph("Module 03: Node.js and npm Setup (Hour 2: 01:00 - 01:30)", h2_style))
    story.append(make_callout(
        "If React runs in the browser, why do we need Node.js? Browsers understand plain JavaScript, not JSX or Vite tooling. Node.js is our local build runtime. npm is our package store. In your project, package.json is the project manifest, package-lock.json locks exact versions, and node_modules holds downloaded libraries. Never edit or commit node_modules!",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(make_code_box(
        "node -v                  # Verify Node.js version (v18+ or v20+ recommended)\n"
        "npm -v                   # Verify npm version\n"
        "npm init -y              # Initialize sample package.json\n"
        "npm i canvas-confetti    # Regular dependency\n"
        "npm i -D vite            # Dev dependency"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Students log results in <code>programs/terminal-commands.txt</code> and complete <code>exercises/exercise-npm-packages.txt</code>."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 4 & 5
    story.append(Paragraph("Modules 04 & 05: Vite Project Creation & Project Structure (Hour 2: 01:30 - 02:00)", h2_style))
    story.append(make_callout(
        "Create-React-App is deprecated because Webpack bundled everything upfront, taking 30-60 seconds to start. Vite (French for 'fast') uses native browser ES modules and pre-bundles using esbuild written in Go. It starts in milliseconds! When Vite runs, index.html loads with <div id='root'>, main.jsx executes ReactDOM.createRoot(), and App.jsx is mounted. StrictMode runs components twice in dev mode to detect side effects.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(make_code_box(
        "npm create vite@latest my-first-react-app -- --template react\n"
        "cd my-first-react-app\n"
        "npm install\n"
        "npm run dev       # Starts dev server on http://localhost:5173"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Demonstrate Hot Module Replacement (HMR): Edit <code>src/App.jsx</code>, save, and show instant browser update."), bullet_style))
    story.append(Paragraph(safe_p("• In <code>05-understanding-project-structure/programs/root-render-practice.jsx</code>, trace the bridge from <code>index.html</code> to <code>main.jsx</code>."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 6
    story.append(Paragraph("Module 06: JSX Syntax and Expressions (Hour 3: 02:00 - 03:00)", h2_style))
    story.append(make_callout(
        "JSX stands for JavaScript XML. It is syntactic sugar for React.createElement(). Golden rules: 1) Every component must return a single root element; use React Fragments (<> ... </>) to avoid extra DOM divs. 2) Close all tags, including <img /> and <input />. 3) Use camelCase attributes like className and htmlFor. 4) The curly braces {} are your portal into JavaScript mode! Any variable, calculation, or ternary condition can be evaluated inside {}.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Open <code>06-jsx-syntax-and-expressions/programs/jsx-syntax-practice.jsx</code>."), bullet_style))
    story.append(Paragraph(safe_p("• Walk through dynamic expressions: <code>{studentName.toUpperCase()}</code> and conditional badges."), bullet_style))
    story.append(Paragraph(safe_p("• <b>Lab Exercise (15 mins):</b> Have students open <code>exercises/exercise-jsx-fixes-and-expressions.jsx</code> and fix the 5 intentional syntax bugs. Walk around the room to verify fixes!"), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 7
    story.append(Paragraph("Module 07: Functional Components (Hour 4: 03:00 - 04:00)", h2_style))
    story.append(make_callout(
        "Components are like LEGO bricks. A functional component is a JavaScript function that returns JSX. Rule 1: The name MUST start with an uppercase letter (PascalCase). If you name it profileCard(), React thinks it is an unknown HTML tag! If you name it ProfileCard(), React knows it is a component. Rule 2: Use default export for the primary component in a file, and named exports for reusable utility components.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Open <code>07-functional-components/programs/functional-components-practice.jsx</code>."), bullet_style))
    story.append(Paragraph(safe_p("• Show composition: <code>InstitutionBadge</code> and <code>PrimaryButton</code> nested inside <code>StudentCard</code>."), bullet_style))
    story.append(Paragraph(safe_p("• <b>Lab Exercise:</b> Students open <code>exercises/exercise-modular-cards.jsx</code> to build <code>DepartmentBadge</code> and <code>StatusBadge</code>."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 8
    story.append(Paragraph("Module 08: Component Rendering (Hour 5: 04:00 - 05:00)", h2_style))
    story.append(make_callout(
        "How do we render real-world dynamic data? In React, we use the JavaScript array method .map() because it returns an array of JSX elements. When mapping, React demands a unique key prop for each element. Why? The key gives elements a stable identity so React's diffing algorithm knows which items changed, moved, or were deleted. Never use array index for dynamic or sortable lists—always use a stable unique ID!",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Open <code>08-component-rendering/programs/list-rendering-practice.jsx</code>. Demonstrate rendering student tables with keys."), bullet_style))
    story.append(Paragraph(safe_p("• Remove the key prop to show students the red browser console warning."), bullet_style))
    story.append(Paragraph(safe_p("• <b>Lab Exercise:</b> Students open <code>exercises/exercise-list-rendering.jsx</code> to map courses and render PASS/ARREAR status tags."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 9
    story.append(Paragraph("Module 09: Practical Project - Student Profile Dashboard (Hour 6: 05:00 - 05:40)", h2_style))
    story.append(make_callout(
        "Now comes our capstone practical! You will assemble a real, running Student Profile Dashboard using all the concepts learned today: functional components, JSX expressions, component composition, and list rendering. We will take the mock dataset in programs/student-data.js and create 5 modular components: Header, ProfileCard, AcademicStats, SkillsList, and ContactCard.",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(make_code_box(
        "cd day-01-introduction-to-react-and-jsx/09-practical-student-profile-dashboard/programs/student-dashboard\n"
        "npm create vite@latest . -- --template react\n"
        "npm install\n"
        "npm run dev"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Guide students to copy <code>student-data.js</code> into their <code>src/</code> folder."), bullet_style))
    story.append(Paragraph(safe_p("• Walk through assembling the 5 components inside <code>App.jsx</code>."), bullet_style))
    story.append(Paragraph(safe_p("• Bonus Challenge from <code>exercises/exercise-dashboard-features.md</code>: Add an attendance warning alert if attendance < 75%."), bullet_style))
    story.append(Spacer(1, 8))

    # Topic 10
    story.append(Paragraph("Module 10: Placement Focus & Mock Interview Drill (Hour 6: 05:40 - 06:00)", h2_style))
    story.append(make_callout(
        "In technical campus rounds, recruiters test whether you understand core principles rather than memorized code. Let's do a 60-second rapid-fire drill. When asked 'Why React?', explain declarative UI and the Virtual DOM. When asked 'Why key prop?', explain identity during reconciliation. Let's open programs/interview-coding-practice.jsx and code the candidate tracker and bounded counter live!",
        "TUTOR SPOKEN SCRIPT:"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(safe_p("• Run through the top 5 interview questions with model answers."), bullet_style))
    story.append(Paragraph(safe_p("• Pair up students to conduct the 60-second mock interview drill in <code>exercises/exercise-placement-mock-interview.md</code>."), bullet_style))
    story.append(Spacer(1, 10))

    # Section 3: Troubleshooting Cheat Sheet
    story.append(Paragraph("3. Tutor Troubleshooting Cheat Sheet (Common Student Errors)", h1_style))
    tb_data = [
        [Paragraph("Symptom / Error", th_style), Paragraph("Root Cause", th_style), Paragraph("Tutor 10-Second Fix", th_style)],
        [Paragraph(safe_p("<code>npm: command not found</code>"), td_bold), Paragraph("Node.js not on system PATH", td_style), Paragraph("Restart terminal; re-run Node installer with 'Add to PATH' checked.", td_style)],
        [Paragraph(safe_p("<code>Adjacent JSX elements must be wrapped</code>"), td_bold), Paragraph("Returning multiple sibling tags", td_style), Paragraph(safe_p("Wrap with React Fragment <code>&lt;&gt; ... &lt;/&gt;</code>."), td_style)],
        [Paragraph(safe_p("Tag <code>&lt;img&gt;</code> throws syntax error"), td_bold), Paragraph("Void tag not closed in JSX", td_style), Paragraph(safe_p("Add self-closing slash: <code>&lt;img src='...' /&gt;</code>."), td_style)],
        [Paragraph("Component rendered as HTML string", td_bold), Paragraph("Lowercase component name", td_style), Paragraph("Rename to PascalCase: <code>function Card()</code>.", td_style)],
        [Paragraph("Warning: <code>Each child in list needs key</code>", td_bold), Paragraph("Missing key in <code>.map()</code>", td_style), Paragraph("Add <code>key={item.id}</code> to outer mapped element.", td_style)],
        [Paragraph("Vite port 5173 in use", td_bold), Paragraph("Another server running", td_style), Paragraph("Vite auto-switches to 5174 or kill process.", td_style)],
        [Paragraph("Git push rejected / frozen", td_bold), Paragraph("Committed node_modules", td_style), Paragraph("Run <code>git rm -r --cached node_modules</code>, commit, push.", td_style)]
    ]
    tb_table = Table(tb_data, colWidths=[140, 160, 232])
    tb_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#d97706')),
        ('PADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#fffbeb')])
    ]))
    story.append(tb_table)
    story.append(Spacer(1, 10))

    # Section 4: Evaluation Rubric
    story.append(Paragraph("4. Student Evaluation Rubric (End of Day 1)", h1_style))
    rubric_data = [
        [Paragraph("Evaluation Criteria", th_style), Paragraph("Max Marks", th_style), Paragraph("What Tutor Verifies", th_style)],
        [Paragraph(safe_p("<b>Notes & Terminologies</b>"), td_style), Paragraph("20 Marks", td_bold), Paragraph("All 10 notes/notes.md files filled with accurate definitions.", td_style)],
        [Paragraph(safe_p("<b>Hands-on Exercises</b>"), td_style), Paragraph("30 Marks", td_bold), Paragraph("Completed exercises in exercises/ folders across modules.", td_style)],
        [Paragraph(safe_p("<b>Student Profile Dashboard</b>"), td_style), Paragraph("35 Marks", td_bold), Paragraph("Running Vite app, 5 modular components, clean CSS layout.", td_style)],
        [Paragraph(safe_p("<b>Placement Readiness</b>"), td_style), Paragraph("15 Marks", td_bold), Paragraph("Verbal clarity during the 60-second mock interview drill.", td_style)],
        [Paragraph("<b>TOTAL</b>", th_style), Paragraph("100 Marks", th_style), Paragraph("<b>Passing Grade: 70%+</b>", th_style)]
    ]
    rubric_table = Table(rubric_data, colWidths=[150, 80, 302])
    rubric_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#1e3a8a')),
        ('PADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    story.append(rubric_table)

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {filename}")

if __name__ == '__main__':
    build_pdf("e:\\mohammed sathak\\Tutor-Guide-Day-01-React-and-JSX.pdf")
