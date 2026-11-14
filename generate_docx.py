import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# ==============================================================================
# COLOR PALETTE
# ==============================================================================
COLOR_PRIMARY_NAVY = RGBColor(30, 58, 138)   # #1E3A8A
COLOR_DARK_TEXT    = RGBColor(15, 23, 42)    # #0F172A
COLOR_BODY_TEXT    = RGBColor(51, 65, 85)    # #334155
COLOR_MUTED_TEXT   = RGBColor(100, 116, 139) # #64748B
COLOR_ACCENT_BLUE  = RGBColor(2, 132, 199)   # #0284C7
COLOR_GREEN        = RGBColor(5, 150, 105)   # #059669
COLOR_AMBER        = RGBColor(217, 119, 6)   # #D97706

# Helper for XML shading
def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_callout(doc, quote_text, title="TUTOR TALKING SCRIPT (Say this to the class):"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "EFF6FF") # Light blue tint
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border styling in XML
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="0284C7"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    r_title = p.add_run(f"🎙️ {title}\n")
    r_title.bold = True
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(9.5)
    r_title.font.color.rgb = COLOR_ACCENT_BLUE
    
    r_quote = p.add_run(f'"{quote_text}"')
    r_quote.italic = True
    r_quote.font.name = "Segoe UI"
    r_quote.font.size = Pt(9.5)
    r_quote.font.color.rgb = COLOR_PRIMARY_NAVY
    
    # Add small spacing after table
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)

def add_code_block(doc, code_text, label=None):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC") # Very light slate
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    
    if label:
        r_lbl = p.add_run(f"💻 {label}\n")
        r_lbl.bold = True
        r_lbl.font.name = "Segoe UI"
        r_lbl.font.size = Pt(8.5)
        r_lbl.font.color.rgb = COLOR_DARK_TEXT
    
    r_code = p.add_run(code_text)
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(8.5)
    r_code.font.color.rgb = COLOR_DARK_TEXT
    
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(4)

# ==============================================================================
# BUILD DOCUMENT
# ==============================================================================
def create_tutor_docx(filename="Tutor_Session_Guide_React_and_JSX.docx"):
    doc = Document()
    
    # Page setup: Margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        # Header & Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("React & JSX Masterclass | Tutor Delivery Playbook")
        hrun.font.name = "Segoe UI"
        hrun.font.size = Pt(8)
        hrun.font.color.rgb = COLOR_MUTED_TEXT

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Complete Classroom Flow • Simple Analogies • Minimal Code • Placement Drill")
        frun.font.name = "Segoe UI"
        frun.font.size = Pt(8)
        frun.font.color.rgb = COLOR_MUTED_TEXT

    # --------------------------------------------------------------------------
    # TITLE SECTION
    # --------------------------------------------------------------------------
    p_badge = doc.add_paragraph()
    p_badge.paragraph_format.space_before = Pt(0)
    p_badge.paragraph_format.space_after = Pt(4)
    r_b = p_badge.add_run("FRONTEND ENGINEERING MASTERCLASS • TUTOR PLAYBOOK")
    r_b.bold = True
    r_b.font.name = "Segoe UI"
    r_b.font.size = Pt(9.5)
    r_b.font.color.rgb = COLOR_ACCENT_BLUE

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run("Introduction to React & JSX")
    r_t.bold = True
    r_t.font.name = "Segoe UI"
    r_t.font.size = Pt(24)
    r_t.font.color.rgb = COLOR_PRIMARY_NAVY

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    r_s = p_sub.add_run("How to Lead the 6-Hour Session: Starting Point, Chronological Flow, Simple Analogies, Minimal Programs & Placement Interview Prep")
    r_s.font.name = "Segoe UI"
    r_s.font.size = Pt(11)
    r_s.font.color.rgb = COLOR_MUTED_TEXT

    # --------------------------------------------------------------------------
    # SECTION 1: MASTER CLASSROOM TIMELINE (THE 4 PHASES)
    # --------------------------------------------------------------------------
    h1 = doc.add_heading("1. Master Session Roadmap (The 4 Phases)", level=1)
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(6)
    for r in h1.runs:
        r.font.name = "Segoe UI"
        r.font.color.rgb = COLOR_PRIMARY_NAVY

    # Timeline Table
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ["Phase", "Time Window", "Core Focus", "Key Classroom Action"]
    col_widths = [Inches(1.2), Inches(1.1), Inches(2.2), Inches(2.0)]
    
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.width = col_widths[c_idx]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Segoe UI"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)

    timeline_data = [
        ("Phase 1", "00:00 - 01:00\n(Hour 1)", "The 'Aha!' Moment:\nHTML, CSS, JS vs React, SPA, Virtual DOM", "Side-by-side live demo of Vanilla JS counter vs React counter. Zero setup required."),
        ("Phase 2", "01:00 - 02:00\n(Hour 2)", "Developer Workshop:\nNode.js, npm & Vite Bullet Train", "Verify node -v; scaffold Vite React app live in 200ms; tour index.html to App.jsx."),
        ("Phase 3", "02:15 - 04:15\n(Hours 3-4)", "The 3 Building Blocks:\nJSX, Components, .map() & Keys", "Master curly braces {}, PascalCase rule, and list rendering without confusing errors."),
        ("Phase 4", "04:15 - 06:00\n(Hours 5-6)", "Hands-On Capstone & Placement Prep", "Students build 25-line Student Dashboard; 60-second mock interview drills.")
    ]

    for row_idx, data in enumerate(timeline_data):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.width = col_widths[col_idx]
            bg = "FFFFFF" if row_idx % 2 == 0 else "F8FAFC"
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 90, 90)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Segoe UI"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK_TEXT
            if col_idx == 0:
                r.bold = True

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(6)

    # --------------------------------------------------------------------------
    # SECTION 2: STEP-BY-STEP TEACHING SCRIPT & FLOW
    # --------------------------------------------------------------------------
    h2 = doc.add_heading("2. Step-by-Step Delivery Script: Where to Start & How to Flow", level=1)
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(6)
    for r in h2.runs:
        r.font.name = "Segoe UI"
        r.font.color.rgb = COLOR_PRIMARY_NAVY

    # Phase 1 Steps
    p_p1 = doc.add_paragraph()
    r = p_p1.add_run("PHASE 1: The 'Aha!' Moment (00:00 - 01:00)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(12)
    r.font.color.rgb = COLOR_ACCENT_BLUE

    add_callout(
        doc,
        "Good morning everyone! Look at Gmail or Netflix on your phone. When you click an email or tap a movie, does the whole browser screen turn white and reload? No! Only the small box in the middle changes. That is what we call a Single Page Application (SPA). Today, we will understand how modern web apps achieve this, and how you will build your first React dashboard before leaving this room.",
        "STEP 1: The 10-Minute Hook (00:00 - 00:10)"
    )

    p_action1 = doc.add_paragraph()
    p_action1.paragraph_format.space_after = Pt(4)
    r = p_action1.add_run("• Whiteboard Analogy to Draw:\n")
    r.bold = True
    p_action1.add_run("   1. HTML = Skeleton / Bones (what exists on the page)\n"
                     "   2. CSS = Skin, Clothes & Paint (colors, fonts, styling)\n"
                     "   3. JavaScript = Brain & Muscles (actions, clicks, calculations)\n"
                     "   4. Vanilla JS = Plain vanilla ice cream with zero toppings (raw browser JS)")

    add_callout(
        doc,
        "Let's see what happens if we write a simple counter in plain Vanilla JS. We have to manually write document.getElementById('btn'), add an event listener, update innerText, and force the browser to recalculate the whole screen. Imagine if you had 50 buttons and 10 forms! One tiny spelling mistake, and your whole website stops working. React was created by Facebook to eliminate this mess.",
        "STEP 2: The Live Comparison Demo (00:10 - 00:35)"
    )

    p_action2 = doc.add_paragraph()
    p_action2.paragraph_format.space_after = Pt(4)
    r = p_action2.add_run("• On-Screen Execution Action:\n")
    r.bold = True
    p_action2.add_run("   1. Double-click traditional-web-demo.html on projector. Click the counter. Point to document.getElementById.\n"
                     "   2. Double-click react-standalone-demo.html. Show the React counter: const [count, setCount] = useState(0). Point out that there is ZERO document.getElementById!")

    add_callout(
        doc,
        "Why is React so fast? Think of the Real DOM as a heavy concrete statue. If you want to change its hat, you need cranes and chisels. The Virtual DOM is a quick pencil sketch on paper in memory. React erases the hat on paper in 1 millisecond (Diffing), and then updates ONLY that 1 inch on the real statue (Reconciliation).",
        "STEP 3: The Virtual DOM in 60 Seconds (00:35 - 01:00)"
    )

    # Phase 2 Steps
    p_p2 = doc.add_paragraph()
    p_p2.paragraph_format.space_before = Pt(8)
    r = p_p2.add_run("PHASE 2: The Developer Workshop (01:00 - 02:00)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(12)
    r.font.color.rgb = COLOR_ACCENT_BLUE

    add_callout(
        doc,
        "Students often ask: 'If React runs in the browser, why do we need Node.js on our computer?' Browsers only understand plain JavaScript—not JSX or modern tools. Node.js is the workshop engine on your laptop that powers our development tools. npm is the world's biggest grocery store for code: instead of writing 1,000 lines for icons or charts, you install ready-made packages.",
        "STEP 4: Node.js & npm (01:00 - 01:25)"
    )

    add_code_block(
        doc,
        "node -v          # Verify Node.js version (v18+ or v20+ recommended)\n"
        "npm -v           # Verify npm version\n"
        "package.json     # Your shopping receipt (lists installed libraries)\n"
        "node_modules/    # The grocery pantry (NEVER commit to Git!)",
        "Terminal Verification Commands"
    )

    add_callout(
        doc,
        "In older tutorials, people used Create-React-App, which took 60 seconds to start. We use Vite (pronounced 'Veet', French for fast). Vite starts your local server in 0.2 seconds! Watch this terminal command.",
        "STEP 5: Scaffolding with Vite (01:25 - 01:50)"
    )

    add_code_block(
        doc,
        "npm create vite@latest my-app -- --template react\n"
        "cd my-app\n"
        "npm install\n"
        "npm run dev       # Starts dev server on http://localhost:5173",
        "Vite Scaffolding Commands"
    )

    p_action3 = doc.add_paragraph()
    p_action3.paragraph_format.space_after = Pt(4)
    r = p_action3.add_run("• The Magic Moment: ")
    r.bold = True
    p_action3.add_run("Open src/App.jsx on screen. Edit the text inside <h1>, hit Ctrl+S, and show students how the browser updates instantly without a page refresh (Hot Module Replacement - HMR)!")

    # Phase 3 Steps
    p_p3 = doc.add_paragraph()
    p_p3.paragraph_format.space_before = Pt(8)
    r = p_p3.add_run("PHASE 3: The 3 Core Building Blocks (02:15 - 04:15)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(12)
    r.font.color.rgb = COLOR_ACCENT_BLUE

    add_callout(
        doc,
        "JSX is HTML and JavaScript getting married! You can write HTML tags directly inside a JS file. Remember the 3 golden rules: 1) Every component must return one single box—use Fragments <> ... </> to avoid extra <div> clutter. 2) Close every tag, even <img />. 3) Use className instead of class.",
        "STEP 7: JSX Syntax & The Curly Braces {} (02:15 - 02:55)"
    )

    add_callout(
        doc,
        "Think of components like LEGO bricks. To build a castle, you snap together standard bricks. In React, a component is a JavaScript function that returns JSX. Golden Rule: Component names MUST start with a Capital Letter (PascalCase)! If you write <profileCard />, React thinks it's a regular HTML tag. If you write <ProfileCard />, React executes your component function.",
        "STEP 8: Functional Components & PascalCase (02:55 - 03:35)"
    )

    add_callout(
        doc,
        "How do we show a list of 50 students in React? We don't write 50 <li> tags by hand. We use the JavaScript array method .map() because it returns an array of JSX elements. When mapping, React demands a unique 'key' prop for each item—like a student roll number during attendance. Without a key, React gets confused which item changed.",
        "STEP 9: List Rendering with .map() and Keys (03:35 - 04:15)"
    )

    # Phase 4 Steps
    p_p4 = doc.add_paragraph()
    p_p4.paragraph_format.space_before = Pt(8)
    r = p_p4.add_run("PHASE 4: Hands-On Capstone & Placement Prep (04:15 - 06:00)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(12)
    r.font.color.rgb = COLOR_ACCENT_BLUE

    add_callout(
        doc,
        "Now it's your turn! Every student will write a 25-line Student Profile Dashboard in their Vite project. We will display a student's name, roll number, department, CGPA, and a list of skills using .map(). You will have a running React app on your computer to show for your resume.",
        "STEP 10: Guided Student Profile Dashboard Lab (04:15 - 05:25)"
    )

    add_callout(
        doc,
        "In technical campus rounds, recruiters test your fundamentals, not just syntax. Let's do a 60-second rapid-fire drill. When asked 'Why React?', say: 'Declarative UI and Virtual DOM.' When asked 'Why key prop?', say: 'Provides element identity during reconciliation.'",
        "STEP 11: Placement Rapid-Fire Interview Drill (05:25 - 05:55)"
    )

    # --------------------------------------------------------------------------
    # SECTION 3: THE 3 COMPLETE ULTRA-SIMPLE PROGRAMS
    # --------------------------------------------------------------------------
    doc.add_page_break()
    h3 = doc.add_heading("3. The 3 Ultra-Simple Sample Programs (No Complex Code!)", level=1)
    h3.paragraph_format.space_before = Pt(10)
    h3.paragraph_format.space_after = Pt(6)
    for r in h3.runs:
        r.font.name = "Segoe UI"
        r.font.color.rgb = COLOR_PRIMARY_NAVY

    p_intro = doc.add_paragraph()
    p_intro.add_run("These 3 programs are stripped of all heavy styling and complex boilerplate. Each takes less than 30 seconds to read and understand.")

    # Program 1
    p_pr1 = doc.add_paragraph()
    r = p_pr1.add_run("PROGRAM 1: Simple Vanilla JS Counter (20 Lines)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_PRIMARY_NAVY

    code_vjs = (
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<body style='font-family: sans-serif; padding: 20px;'>\n"
        "  <h2>Vanilla JS Counter</h2>\n"
        "  <h1 id='count'>0</h1>\n"
        "  <button id='btn'>+ Add</button>\n\n"
        "  <script>\n"
        "    let n = 0;\n"
        "    const text = document.getElementById('count');\n"
        "    const button = document.getElementById('btn');\n\n"
        "    button.addEventListener('click', function() {\n"
        "      n = n + 1;\n"
        "      text.innerText = n; // Manual DOM update\n"
        "    });\n"
        "  </script>\n"
        "</body>\n"
        "</html>"
    )
    add_code_block(doc, code_vjs, "traditional-web-demo.html")

    # Program 2
    p_pr2 = doc.add_paragraph()
    r = p_pr2.add_run("PROGRAM 2: Simple Standalone React App (State + Props + List, 35 Lines)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_PRIMARY_NAVY

    code_react = (
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        "  <!-- React & Babel from CDN (No setup required) -->\n"
        "  <script src='https://unpkg.com/react@18/umd/react.development.js' crossorigin></script>\n"
        "  <script src='https://unpkg.com/react-dom@18/umd/react-dom.development.js' crossorigin></script>\n"
        "  <script src='https://unpkg.com/@babel/standalone/babel.min.js'></script>\n"
        "</head>\n"
        "<body style='font-family: sans-serif; padding: 20px;'>\n"
        "  <div id='root'></div>\n\n"
        "  <script type='text/babel'>\n"
        "    const { useState } = React;\n\n"
        "    // 1. Component with a PROP\n"
        "    function Greeting({ name }) {\n"
        "      return <h2>Hello, {name}!</h2>;\n"
        "    }\n\n"
        "    // 2. Main App with STATE and a LIST\n"
        "    function App() {\n"
        "      const [count, setCount] = useState(0);\n"
        "      const skills = ['HTML', 'CSS', 'JavaScript', 'React'];\n\n"
        "      return (\n"
        "        <div>\n"
        "          <Greeting name='Student' />\n"
        "          <button onClick={() => setCount(count + 1)}>Clicks: {count}</button>\n"
        "          <h3>My Skills:</h3>\n"
        "          <ul>\n"
        "            {skills.map(s => <li key={s}>{s}</li>)}\n"
        "          </ul>\n"
        "        </div>\n"
        "      );\n"
        "    }\n\n"
        "    ReactDOM.createRoot(document.getElementById('root')).render(<App />);\n"
        "  </script>\n"
        "</body>\n"
        "</html>"
    )
    add_code_block(doc, code_react, "react-standalone-demo.html")

    # Program 3
    p_pr3 = doc.add_paragraph()
    r = p_pr3.add_run("PROGRAM 3: Practical Student Profile Dashboard (Vite App.jsx, 25 Lines)")
    r.bold = True
    r.font.name = "Segoe UI"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_PRIMARY_NAVY

    code_dash = (
        "import React from 'react';\n\n"
        "export default function App() {\n"
        "  const student = {\n"
        "    name: 'Alex',\n"
        "    rollNo: '101',\n"
        "    dept: 'Computer Science',\n"
        "    cgpa: 8.9,\n"
        "    skills: ['HTML', 'CSS', 'JavaScript', 'React']\n"
        "  };\n\n"
        "  return (\n"
        "    <div style={{ padding: '16px', border: '1px solid #ccc', maxWidth: '300px', fontFamily: 'sans-serif' }}>\n"
        "      <h2>Student Dashboard</h2>\n"
        "      <p>Name: <b>{student.name}</b></p>\n"
        "      <p>Roll No: {student.rollNo}</p>\n"
        "      <p>Department: {student.dept}</p>\n"
        "      <p>CGPA: {student.cgpa}</p>\n\n"
        "      <h4>Skills:</h4>\n"
        "      <ul>\n"
        "        {student.skills.map((skill) => (\n"
        "          <li key={skill}>{skill}</li>\n"
        "        ))}\n"
        "      </ul>\n"
        "    </div>\n"
        "  );\n"
        "}"
    )
    add_code_block(doc, code_dash, "src/App.jsx (in Vite project)")

    # --------------------------------------------------------------------------
    # SECTION 4: PLACEMENT INTERVIEW QUESTIONS & 30-SECOND ANSWERS
    # --------------------------------------------------------------------------
    h4 = doc.add_heading("4. Placement Technical Interview Drill (Top 5 Questions)", level=1)
    h4.paragraph_format.space_before = Pt(12)
    h4.paragraph_format.space_after = Pt(6)
    for r in h4.runs:
        r.font.name = "Segoe UI"
        r.font.color.rgb = COLOR_PRIMARY_NAVY

    qa_list = [
        ("Q1: Is React a library or framework?", "React is a library. It focuses solely on building the user interface (the View layer of MVC), giving developers the freedom to choose their own routing, state management, and build tools."),
        ("Q2: What is the Virtual DOM and why is it faster?", "The Virtual DOM is a lightweight copy of the Real DOM kept in memory. When state changes, React compares the old and new trees using an O(n) diffing algorithm and updates ONLY the changed nodes in the real DOM, avoiding expensive browser reflows."),
        ("Q3: Why can't browsers read JSX directly?", "JSX is not valid ECMAScript. It is syntactic sugar for React.createElement() function calls and must be compiled by Babel or esbuild before running in the browser."),
        ("Q4: Why must component names start with an uppercase letter?", "React uses casing to distinguish between native HTML elements (<button>, <div>) and custom React components (<ProfileCard />)."),
        ("Q5: Why is the 'key' prop mandatory when rendering lists?", "Keys provide a stable identity across renders. When array items are added, deleted, or reordered, React uses the key to track changes without re-rendering the entire list.")
    ]

    for q, a in qa_list:
        p_qa = doc.add_paragraph()
        p_qa.paragraph_format.space_before = Pt(4)
        p_qa.paragraph_format.space_after = Pt(4)
        r_q = p_qa.add_run(f"• {q}\n")
        r_q.bold = True
        r_q.font.name = "Segoe UI"
        r_q.font.size = Pt(9.5)
        r_q.font.color.rgb = COLOR_PRIMARY_NAVY
        
        r_a = p_qa.add_run(f"   Model Answer: {a}")
        r_a.font.name = "Segoe UI"
        r_a.font.size = Pt(9)
        r_a.font.color.rgb = COLOR_BODY_TEXT

    # --------------------------------------------------------------------------
    # SECTION 5: TUTOR TROUBLESHOOTING CHEAT SHEET
    # --------------------------------------------------------------------------
    h5 = doc.add_heading("5. Tutor Troubleshooting Cheat Sheet (10-Second Fixes)", level=1)
    h5.paragraph_format.space_before = Pt(12)
    h5.paragraph_format.space_after = Pt(6)
    for r in h5.runs:
        r.font.name = "Segoe UI"
        r.font.color.rgb = COLOR_PRIMARY_NAVY

    tbl_err = doc.add_table(rows=6, cols=3)
    tbl_err.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_err.autofit = False

    err_widths = [Inches(2.0), Inches(2.2), Inches(2.3)]
    err_headers = ["Student Error / Symptom", "Root Cause", "Tutor 10-Second Fix"]

    for c_idx, h in enumerate(err_headers):
        cell = tbl_err.cell(0, c_idx)
        cell.width = err_widths[c_idx]
        set_cell_background(cell, "D97706") # Amber header
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Segoe UI"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)

    err_data = [
        ("npm: command not found", "Node.js not on system PATH", "Restart terminal; re-run Node installer with 'Add to PATH' checked."),
        ("Adjacent JSX elements must be wrapped", "Returning multiple sibling tags", "Wrap the tags inside a React Fragment: <> ... </>"),
        ("Tag <img> throws syntax error", "Void tag not self-closed in JSX", "Add a self-closing slash: <img src='...' />"),
        ("Component renders as raw text", "Component name is lowercase", "Rename to PascalCase: function Card() instead of function card()"),
        ("Warning: Each child in list needs key", "Missing key prop inside .map()", "Add key={item} to the outermost tag returned inside .map()")
    ]

    for row_idx, data in enumerate(err_data):
        for col_idx, text in enumerate(data):
            cell = tbl_err.cell(row_idx + 1, col_idx)
            cell.width = err_widths[col_idx]
            bg = "FFFFFF" if row_idx % 2 == 0 else "FFFBEB"
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 90, 90)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Segoe UI"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK_TEXT
            if col_idx == 0:
                r.bold = True

    # Save document
    doc.save(filename)
    print(f"DOCX created successfully: {filename}")

if __name__ == '__main__':
    create_tutor_docx("e:\\mohammed sathak\\Tutor_Session_Guide_React_and_JSX.docx")

