import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# COLOR PALETTE (Modern Slate & React Cyan Theme)
# ==============================================================================
BG_COLOR       = RGBColor(15, 23, 42)     # Slate 900 (#0F172A)
CARD_BG        = RGBColor(30, 41, 59)     # Slate 800 (#1E293B)
CARD_BORDER    = RGBColor(51, 65, 85)     # Slate 700 (#334155)
CARD_ALT_BG    = RGBColor(24, 33, 47)     # Darker card (#18212F)

TEXT_TITLE     = RGBColor(255, 255, 255)  # Pure White
TEXT_BODY      = RGBColor(226, 232, 240)  # Slate 200
TEXT_MUTED     = RGBColor(148, 163, 184)  # Slate 400

ACCENT_CYAN    = RGBColor(56, 189, 248)   # React Cyan / Sky 400 (#38BDF8)
ACCENT_INDIGO  = RGBColor(129, 140, 248)  # Indigo 400 (#818CF8)
ACCENT_GREEN   = RGBColor(52, 211, 153)   # Emerald 400 (#34D399)
ACCENT_AMBER   = RGBColor(251, 191, 36)   # Amber 400 (#FBBF24)
ACCENT_ROSE    = RGBColor(251, 113, 133)  # Rose 400 (#FB7185)

CODE_BG        = RGBColor(10, 15, 30)     # Dark terminal (#0A0F1E)
CODE_BORDER    = RGBColor(40, 50, 70)

FONT_HEADING = 'Segoe UI'
FONT_BODY    = 'Segoe UI'
FONT_CODE    = 'Consolas'

# ==============================================================================
# HELPER FUNCTIONS FOR CLEAN PPTX GENERATION
# ==============================================================================

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def set_slide_background(slide):
    # Add full slide background shape
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5)
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()
    return bg

def add_header(slide, category, title, subtitle=None):
    set_slide_background(slide)
    
    # Category Tag Pill
    cat_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(3.2), Inches(0.35)
    )
    cat_box.fill.solid()
    cat_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    cat_box.line.color.rgb = ACCENT_CYAN
    cat_box.line.width = Pt(1)
    
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf_c.margin_left = tf_c.margin_right = tf_c.margin_top = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.name = FONT_HEADING
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = ACCENT_CYAN
    p_c.alignment = PP_ALIGN.CENTER

    # Main Title & Subtitle Box
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.733), Inches(1.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_HEADING
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = TEXT_TITLE
    p.space_after = Pt(2)
    
    if subtitle:
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = FONT_BODY
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = TEXT_MUTED

def add_card(slide, left, top, width, height, title=None, border_color=CARD_BORDER, bg_color=CARD_BG):
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    
    if title:
        # Title banner inside card
        tb = slide.shapes.add_textbox(Inches(left + 0.25), Inches(top + 0.2), Inches(width - 0.5), Inches(0.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
    return card

def add_bullet(tf, bold_prefix, text, size=11, font_color=TEXT_BODY, space_after=6):
    p = tf.add_paragraph()
    p.space_after = Pt(space_after)
    p.level = 0
    
    run_bold = p.add_run()
    run_bold.text = bold_prefix + " "
    run_bold.font.name = FONT_HEADING
    run_bold.font.bold = True
    run_bold.font.size = Pt(size)
    run_bold.font.color.rgb = TEXT_TITLE
    
    run_text = p.add_run()
    run_text.text = text
    run_text.font.name = FONT_BODY
    run_text.font.size = Pt(size)
    run_text.font.color.rgb = font_color

def add_code_box(slide, left, top, width, height, code_text):
    box = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = CODE_BG
    box.line.color.rgb = CODE_BORDER
    box.line.width = Pt(1)
    
    tb = slide.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(width - 0.3), Inches(height - 0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    
    for i, line in enumerate(code_text.strip().split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        p.font.name = FONT_CODE
        p.font.size = Pt(9.5)
        if line.strip().startswith('//') or line.strip().startswith('#'):
            p.font.color.rgb = ACCENT_GREEN
        elif 'import' in line or 'export' in line or 'return' in line or 'const' in line:
            p.font.color.rgb = ACCENT_INDIGO
        else:
            p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(1)

# ==============================================================================
# SLIDE BUILDERS
# ==============================================================================

def build_deck():
    prs = create_presentation()
    blank_layout = prs.slide_layouts[6]

    # --------------------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # --------------------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    
    # Hero Title Box
    tb_title = slide1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(3.2))
    tf1 = tb_title.text_frame
    tf1.word_wrap = True
    
    p_tag = tf1.paragraphs[0]
    p_tag.text = "FRONTEND ENGINEERING MASTERCLASS"
    p_tag.font.name = FONT_HEADING
    p_tag.font.size = Pt(13)
    p_tag.font.bold = True
    p_tag.font.color.rgb = ACCENT_CYAN
    p_tag.space_after = Pt(12)
    
    p_h1 = tf1.add_paragraph()
    p_h1.text = "Introduction to React & JSX"
    p_h1.font.name = FONT_HEADING
    p_h1.font.size = Pt(40)
    p_h1.font.bold = True
    p_h1.font.color.rgb = TEXT_TITLE
    p_h1.space_after = Pt(10)
    
    p_sub = tf1.add_paragraph()
    p_sub.text = "Single Page Applications, Modern Build Tooling, Component-Driven UI & Placement Focus"
    p_sub.font.name = FONT_BODY
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = TEXT_MUTED
    
    # Feature Badge Pill row
    badges = [
        ("React.js", ACCENT_CYAN),
        ("Single Page Applications", ACCENT_INDIGO),
        ("Vite & ESBuild", ACCENT_GREEN),
        ("JSX Syntax", ACCENT_AMBER),
        ("Functional Components", ACCENT_CYAN),
        ("Placement Interview Ready", ACCENT_ROSE)
    ]
    
    start_left = 1.0
    for text, color in badges:
        w = 1.8
        badge = slide1.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(start_left), Inches(5.4), Inches(w), Inches(0.55)
        )
        badge.fill.solid()
        badge.fill.fore_color.rgb = CARD_BG
        badge.line.color.rgb = color
        badge.line.width = Pt(1)
        
        tf_b = badge.text_frame
        tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_b = tf_b.paragraphs[0]
        p_b.text = text
        p_b.font.name = FONT_HEADING
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = color
        p_b.alignment = PP_ALIGN.CENTER
        start_left += 1.95

    # --------------------------------------------------------------------------
    # SLIDE 2: CURRICULUM ROADMAP
    # --------------------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Course Structure", "Master Curriculum Roadmap", "Comprehensive 10-module guide to mastering core React fundamentals")
    
    modules = [
        ("01", "Intro to React & SPA", "Component philosophy, CSR, SPA mechanics"),
        ("02", "React vs Traditional Web", "Declarative UI, Real DOM vs Virtual DOM"),
        ("03", "Node.js & npm Setup", "Runtime environment, package management"),
        ("04", "Vite Project Creation", "Next-gen build tooling, ESM, instant HMR"),
        ("05", "Project Structure Anatomy", "index.html, main.jsx, createRoot, App.jsx"),
        ("06", "JSX Syntax & Expressions", "Curly braces {}, fragments, attributes"),
        ("07", "Functional Components", "PascalCase convention, modularity & exports"),
        ("08", "Component Rendering", "Render lifecycle, list rendering with keys"),
        ("09", "Practical Dashboard Project", "Modular Student Profile Dashboard build"),
        ("10", "Placement Focus & Q&A", "High-frequency technical campus interviews")
    ]
    
    for idx, (num, title, desc) in enumerate(modules):
        col = idx % 5
        row = idx // 5
        left = 0.8 + col * 2.4
        top = 2.2 + row * 2.3
        
        c = add_card(slide2, left, top, 2.25, 2.1, None, CARD_BORDER, CARD_BG)
        tb_m = slide2.shapes.add_textbox(Inches(left + 0.15), Inches(top + 0.15), Inches(1.95), Inches(1.8))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_right = tf_m.margin_top = tf_m.margin_bottom = 0
        
        p_num = tf_m.paragraphs[0]
        p_num.text = f"MODULE {num}"
        p_num.font.name = FONT_HEADING
        p_num.font.size = Pt(9)
        p_num.font.bold = True
        p_num.font.color.rgb = ACCENT_CYAN
        p_num.space_after = Pt(3)
        
        p_t = tf_m.add_paragraph()
        p_t.text = title
        p_t.font.name = FONT_HEADING
        p_t.font.size = Pt(11.5)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_TITLE
        p_t.space_after = Pt(4)
        
        p_d = tf_m.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_BODY
        p_d.font.size = Pt(9)
        p_d.font.color.rgb = TEXT_MUTED

    # --------------------------------------------------------------------------
    # SLIDE 3: MODULE 01 - REACT & SPA
    # --------------------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Module 01", "Introduction to React & Single Page Applications", "How modern web architectures eliminate page reloads and improve user experience")
    
    # Left Card: What is React?
    add_card(slide3, 0.8, 2.2, 5.7, 4.7, "What is React?", ACCENT_CYAN)
    tb_c1 = slide3.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_c1 = tb_c1.text_frame
    tf_c1.word_wrap = True
    add_bullet(tf_c1, "Library, Not a Framework:", "React focuses exclusively on the View layer of MVC. Developers choose their own state and routing libraries.")
    add_bullet(tf_c1, "Component-Driven:", "Build independent, reusable user interface building blocks like LEGO bricks.")
    add_bullet(tf_c1, "Created by Meta (Facebook):", "Authored by Jordan Walke in 2011 to solve state synchronization across complex, real-time UI feeds.")
    add_bullet(tf_c1, "Unidirectional Data Flow:", "Data flows cleanly downwards from parent components to child components via props.")

    # Right Card: Single Page Application (SPA) vs Multi-Page (MPA)
    add_card(slide3, 6.8, 2.2, 5.7, 4.7, "SPA vs Traditional MPA Architecture", ACCENT_INDIGO)
    tb_c2 = slide3.shapes.add_textbox(Inches(7.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_c2 = tb_c2.text_frame
    tf_c2.word_wrap = True
    add_bullet(tf_c2, "Single HTML Entry:", "An SPA serves only one HTML file (index.html). The browser never requests new full pages.")
    add_bullet(tf_c2, "Client-Side Rendering (CSR):", "JavaScript executes in the user's browser, fetching raw JSON data from APIs and dynamically updating the DOM.")
    add_bullet(tf_c2, "Instant Native-App UX:", "Navigation occurs without white-screen flashes, maintaining persistent headers, state, and audio/video players.")
    add_bullet(tf_c2, "Real-World Examples:", "Gmail, Netflix, Spotify, Instagram, and modern software-as-a-service platforms.")

    # --------------------------------------------------------------------------
    # SLIDE 4: MODULE 02 - REACT VS TRADITIONAL WEB
    # --------------------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Module 02", "React vs Traditional Web Development", "Contrasting imperative DOM manipulation with declarative UI paradigms")
    
    # Left: Traditional Imperative
    add_card(slide4, 0.8, 2.2, 5.7, 4.7, "Traditional: Imperative Vanilla JS", ACCENT_AMBER)
    tb_t = slide4.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(1.8))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    add_bullet(tf_t, "Step-by-Step Instructions:", "Tells the browser exactly HOW to find, create, and mutate every DOM element.")
    add_bullet(tf_t, "High Coupling & Fragility:", "Direct DOM querying (document.getElementById) breaks easily as application complexity grows.")
    
    code_imp = (
        "// Imperative DOM Mutation\n"
        "const btn = document.getElementById('btn');\n"
        "const display = document.getElementById('count');\n"
        "let count = 0;\n"
        "btn.addEventListener('click', () => {\n"
        "  count++;\n"
        "  display.innerText = `Count: ${count}`;\n"
        "});"
    )
    add_code_box(slide4, 1.05, 4.6, 5.2, 2.0, code_imp)

    # Right: Declarative React
    add_card(slide4, 6.8, 2.2, 5.7, 4.7, "Modern: Declarative React Paradigm", ACCENT_GREEN)
    tb_r = slide4.shapes.add_textbox(Inches(7.05), Inches(2.8), Inches(5.2), Inches(1.8))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    add_bullet(tf_r, "Mathematical Predictability:", "UI = f(State). You declare WHAT the UI should look like for a given state.")
    add_bullet(tf_r, "Automated Synchronization:", "React synchronizes the browser screen whenever underlying state changes.")

    code_dec = (
        "// Declarative React Component\n"
        "function Counter() {\n"
        "  const [count, setCount] = useState(0);\n"
        "  return (\n"
        "    <button onClick={() => setCount(count + 1)}>\n"
        "      Count: {count}\n"
        "    </button>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide4, 7.05, 4.6, 5.2, 2.0, code_dec)

    # --------------------------------------------------------------------------
    # SLIDE 5: MODULE 02 (CONT) - VIRTUAL DOM & RECONCILIATION
    # --------------------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Module 02 (Deep Dive)", "The Virtual DOM & Reconciliation Engine", "Why manipulating the Real DOM is slow and how React optimizes rendering performance")
    
    steps = [
        ("1. In-Memory Representation", "The Virtual DOM (VDOM) is a lightweight JavaScript tree representation of the Real DOM kept in memory by ReactDOM.", ACCENT_CYAN),
        ("2. State Change & Re-render", "When component state changes, React creates a brand-new Virtual DOM tree representing the updated UI state.", ACCENT_INDIGO),
        ("3. The Diffing Algorithm", "React compares the new VDOM with the previous VDOM snapshot using an optimized O(n) heuristic diffing algorithm.", ACCENT_AMBER),
        ("4. Reconciliation & Batching", "React calculates the minimal set of changes and batches updates to ONLY the affected nodes in the Real DOM.", ACCENT_GREEN)
    ]
    
    for idx, (title, desc, color) in enumerate(steps):
        top = 2.2 + idx * 1.15
        card = add_card(slide5, 0.8, top, 11.733, 1.0, None, color, CARD_BG)
        tb_s = slide5.shapes.add_textbox(Inches(1.05), Inches(top + 0.15), Inches(11.2), Inches(0.7))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = tf_s.margin_bottom = 0
        
        p = tf_s.paragraphs[0]
        run_t = p.add_run()
        run_t.text = title + ": "
        run_t.font.name = FONT_HEADING
        run_t.font.bold = True
        run_t.font.size = Pt(13)
        run_t.font.color.rgb = color
        
        run_d = p.add_run()
        run_d.text = desc
        run_d.font.name = FONT_BODY
        run_d.font.size = Pt(11)
        run_d.font.color.rgb = TEXT_BODY

    # --------------------------------------------------------------------------
    # SLIDE 6: MODULE 03 - NODE.JS & NPM SETUP
    # --------------------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Module 03", "Node.js & npm Setup", "Understanding the modern JavaScript runtime, package ecosystem, and dependency management")
    
    add_card(slide6, 0.8, 2.2, 5.7, 4.7, "Why Node.js for Frontend Development?", ACCENT_CYAN)
    tb_n1 = slide6.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_n1 = tb_n1.text_frame
    tf_n1.word_wrap = True
    add_bullet(tf_n1, "Local Build Environment:", "Browsers execute plain JavaScript. They cannot run JSX, bundlers, or CSS preprocessors without Node.js.")
    add_bullet(tf_n1, "npm (Node Package Manager):", "The world's largest registry of open-source software libraries, tooling, and command-line interfaces.")
    add_bullet(tf_n1, "Dependencies vs devDependencies:", "Runtime packages (like Lucide icons, date formatters) vs build-time tooling (Vite, ESLint).")
    add_bullet(tf_n1, "Version Verification:", "Ensure Node.js LTS (v18+ or v20+) and npm v9+ are properly configured in system PATH.")

    add_card(slide6, 6.8, 2.2, 5.7, 4.7, "Critical Configuration & Command Reference", ACCENT_AMBER)
    code_npm = (
        "# 1. Verify Environment Versions\n"
        "node -v\n"
        "npm -v\n\n"
        "# 2. Initialize and Install Packages\n"
        "npm init -y\n"
        "npm install lucide-react      # Production dependency\n"
        "npm install -D vite          # Development dependency\n\n"
        "# 3. Key Files Structure\n"
        "package.json        # Project manifest & run scripts\n"
        "package-lock.json   # Exact dependency version locks\n"
        "node_modules/       # Downloaded libraries (NEVER commit!)"
    )
    add_code_box(slide6, 7.05, 2.8, 5.2, 3.8, code_npm)

    # --------------------------------------------------------------------------
    # SLIDE 7: MODULE 04 - VITE PROJECT CREATION
    # --------------------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Module 04", "Vite: Next-Generation Frontend Tooling", "Why modern web developers replaced Create React App with Vite for blazing-fast builds")
    
    add_card(slide7, 0.8, 2.2, 5.7, 4.7, "Why Vite Over Create React App (CRA)?", ACCENT_GREEN)
    tb_v1 = slide7.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_v1 = tb_v1.text_frame
    tf_v1.word_wrap = True
    add_bullet(tf_v1, "Vite (/vit/ - French for 'Fast'):", "Created by Evan You to fundamentally modernize frontend developer experience.")
    add_bullet(tf_v1, "Native ES Modules (ESM):", "Serves source files over native browser ESM on demand without bundling everything upfront.")
    add_bullet(tf_v1, "Powered by esbuild (Written in Go):", "Pre-bundles dependencies 10x-100x faster than JavaScript-based bundlers like Webpack.")
    add_bullet(tf_v1, "Instant Hot Module Replacement (HMR):", "Updates modified UI components in real time without refreshing the page or losing state.")

    add_card(slide7, 6.8, 2.2, 5.7, 4.7, "Step-by-Step Project Scaffolding", ACCENT_CYAN)
    code_vite = (
        "# Step 1: Scaffold new Vite React project\n"
        "npm create vite@latest my-react-app -- --template react\n\n"
        "# Step 2: Navigate into the directory\n"
        "cd my-react-app\n\n"
        "# Step 3: Install all dependencies\n"
        "npm install\n\n"
        "# Step 4: Start lightning-fast dev server\n"
        "npm run dev\n"
        "# -> Local server active: http://localhost:5173/"
    )
    add_code_box(slide7, 7.05, 2.8, 5.2, 3.8, code_vite)

    # --------------------------------------------------------------------------
    # SLIDE 8: MODULE 05 - UNDERSTANDING PROJECT STRUCTURE
    # --------------------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Module 05", "Understanding Project Structure", "Tracing execution flow from index.html to main.jsx and the root component App.jsx")
    
    # Left: Directory breakdown
    add_card(slide8, 0.8, 2.2, 5.7, 4.7, "Project File Anatomy", ACCENT_INDIGO)
    tb_p1 = slide8.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    add_bullet(tf_p1, "index.html:", "The single entry point of the SPA containing <div id='root'>. Unlike Webpack, it sits in the project root.")
    add_bullet(tf_p1, "src/main.jsx:", "JavaScript entry point that imports React, locates the root div, and mounts the application via createRoot.")
    add_bullet(tf_p1, "src/App.jsx:", "The root component and top-level container of your UI hierarchy.")
    add_bullet(tf_p1, "<React.StrictMode>:", "Development helper that intentionally mounts components twice to highlight accidental side-effects.")
    add_bullet(tf_p1, "public/ vs src/assets/:", "Public assets are served unmodified; assets in src/ are bundled, hashed, and optimized by Vite.")

    # Right: Code mounting
    add_card(slide8, 6.8, 2.2, 5.7, 4.7, "How React Mounts into the Browser", ACCENT_CYAN)
    code_mount = (
        "// src/main.jsx - Execution Bridge\n"
        "import React from 'react';\n"
        "import ReactDOM from 'react-dom/client';\n"
        "import App from './App.jsx';\n"
        "import './index.css';\n\n"
        "// 1. Locate root div in index.html\n"
        "const root = document.getElementById('root');\n\n"
        "// 2. Initialize React Root & Render\n"
        "ReactDOM.createRoot(root).render(\n"
        "  <React.StrictMode>\n"
        "    <App />\n"
        "  </React.StrictMode>\n"
        ");"
    )
    add_code_box(slide8, 7.05, 2.8, 5.2, 3.8, code_mount)

    # --------------------------------------------------------------------------
    # SLIDE 9: MODULE 06 - JSX SYNTAX & RULES
    # --------------------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Module 06", "JSX Syntax & Core Rules", "Demystifying JavaScript XML, compiler transpilation, and strict syntactic guidelines")
    
    add_card(slide9, 0.8, 2.2, 5.7, 4.7, "What is JSX Under the Hood?", ACCENT_AMBER)
    tb_j1 = slide9.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(1.8))
    tf_j1 = tb_j1.text_frame
    tf_j1.word_wrap = True
    add_bullet(tf_j1, "Syntactic Sugar:", "JSX looks like HTML, but compiles into standard React.createElement() function calls.")
    add_bullet(tf_j1, "Browser Incompatibility:", "Browsers cannot parse JSX directly. Babel or esbuild transforms it into pure ECMAScript.")
    
    code_trans = (
        "// What you write (JSX):\n"
        "const card = <h1 className='title'>Hello</h1>;\n\n"
        "// What Babel / Vite outputs (Pure JS):\n"
        "const card = React.createElement(\n"
        "  'h1',\n"
        "  { className: 'title' },\n"
        "  'Hello'\n"
        ");"
    )
    add_code_box(slide9, 1.05, 4.6, 5.2, 2.0, code_trans)

    add_card(slide9, 6.8, 2.2, 5.7, 4.7, "The 4 Mandatory Rules of JSX", ACCENT_GREEN)
    tb_j2 = slide9.shapes.add_textbox(Inches(7.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_j2 = tb_j2.text_frame
    tf_j2.word_wrap = True
    add_bullet(tf_j2, "1. Single Root Element:", "Every component must return one parent element. Wrap siblings in a React Fragment (<> ... </>) to prevent DOM bloat.")
    add_bullet(tf_j2, "2. Explicit Tag Closing:", "All void elements must be self-closed: <img />, <input />, <br />.")
    add_bullet(tf_j2, "3. camelCase Attributes:", "Use className instead of 'class' (JS keyword) and htmlFor instead of 'for'. Event handlers: onClick, onChange.")
    add_bullet(tf_j2, "4. Inline Styles as Objects:", "Styles are written as JavaScript objects with camelCase properties: style={{ backgroundColor: '#1E293B' }}.")

    # --------------------------------------------------------------------------
    # SLIDE 10: MODULE 06 (CONT) - DYNAMIC EXPRESSIONS & CONDITIONALS
    # --------------------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Module 06 (Practice)", "Dynamic Expressions & Conditional Rendering", "Leveraging curly braces {} to evaluate JavaScript dynamically inside markup")
    
    add_card(slide10, 0.8, 2.2, 5.7, 4.7, "The Power of Curly Braces {}", ACCENT_CYAN)
    tb_e1 = slide10.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_e1 = tb_e1.text_frame
    tf_e1.word_wrap = True
    add_bullet(tf_e1, "Portal to JavaScript:", "Whenever you open {}, JSX switches from HTML markup mode into JavaScript execution mode.")
    add_bullet(tf_e1, "What Can Be Evaluated:", "Variables, arithmetic ({2 + 2}), string methods ({name.toUpperCase()}), and function calls.")
    add_bullet(tf_e1, "Expressions vs Statements:", "Only expressions (code that resolves to a value) work inside {}. Statements like 'if', 'for', and 'while' are NOT allowed.")
    add_bullet(tf_e1, "Conditional Rendering:", "Use Ternary Operators (condition ? A : B) and Logical AND (condition && <Component />).")

    add_card(slide10, 6.8, 2.2, 5.7, 4.7, "Practical Code Examples", ACCENT_INDIGO)
    code_expr = (
        "function StudentStatus() {\n"
        "  const studentName = 'Amina';\n"
        "  const attendance = 88;\n"
        "  const isEligible = attendance >= 75;\n\n"
        "  return (\n"
        "    <div className='card'>\n"
        "      {/* Dynamic string evaluation */}\n"
        "      <h2>Student: {studentName.toUpperCase()}</h2>\n\n"
        "      {/* Ternary conditional text */}\n"
        "      <p>Status: {isEligible ? 'Eligible' : 'Shortage'}</p>\n\n"
        "      {/* Logical AND conditional rendering */}\n"
        "      {isEligible && (\n"
        "        <span className='badge-green'>Exam Hall Ticket Ready</span>\n"
        "      )}\n"
        "    </div>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide10, 7.05, 2.8, 5.2, 3.8, code_expr)

    # --------------------------------------------------------------------------
    # SLIDE 11: MODULE 07 - FUNCTIONAL COMPONENTS
    # --------------------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Module 07", "Functional Components Architecture", "Building modular, reusable user interface elements with JavaScript functions")
    
    add_card(slide11, 0.8, 2.2, 5.7, 4.7, "Component Fundamentals & Rules", ACCENT_GREEN)
    tb_f1 = slide11.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_f1 = tb_f1.text_frame
    tf_f1.word_wrap = True
    add_bullet(tf_f1, "What is a Functional Component?", "A regular JavaScript function that accepts inputs (props) and returns JSX describing UI.")
    add_bullet(tf_f1, "The PascalCase Rule (Crucial):", "Component names MUST start with an uppercase letter (e.g. ProfileCard, not profileCard).")
    add_bullet(tf_f1, "Why React Enforces PascalCase:", "React distinguishes between built-in HTML tags (<button>, <div>) and custom components (<Button />).")
    add_bullet(tf_f1, "Default vs Named Exports:", "Default export (one per file: export default App) vs Named export (multiple reusable items: export function Badge).")

    add_card(slide11, 6.8, 2.2, 5.7, 4.7, "Component Composition Example", ACCENT_CYAN)
    code_comp = (
        "// 1. Reusable Child Component (Named Export)\n"
        "export function SkillBadge({ skill }) {\n"
        "  return <span className='badge'>{skill}</span>;\n"
        "}\n\n"
        "// 2. Parent Container Component (Default Export)\n"
        "export default function ProfileHeader() {\n"
        "  return (\n"
        "    <header className='profile-header'>\n"
        "      <h1>Zainab Banu</h1>\n"
        "      <p>Computer Science & Engineering</p>\n"
        "      <div className='skills-container'>\n"
        "        <SkillBadge skill='React.js' />\n"
        "        <SkillBadge skill='JavaScript' />\n"
        "      </div>\n"
        "    </header>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide11, 7.05, 2.8, 5.2, 3.8, code_comp)

    # --------------------------------------------------------------------------
    # SLIDE 12: MODULE 08 - COMPONENT RENDERING & LIFECYCLE
    # --------------------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Module 08", "Component Rendering & Composition", "How React triggers renders, evaluates component trees, and commits changes to the screen")
    
    stages = [
        ("Phase 1: Triggering", "A render is triggered by initial application mounting (createRoot) or state/prop updates.", ACCENT_CYAN),
        ("Phase 2: Rendering", "React executes your component function to calculate what JSX markup needs to appear on screen.", ACCENT_AMBER),
        ("Phase 3: Committing", "React compares the new tree with the previous tree and updates only modified real DOM nodes.", ACCENT_GREEN)
    ]
    
    for idx, (title, desc, color) in enumerate(stages):
        left = 0.8 + idx * 4.0
        c = add_card(slide12, left, 2.2, 3.733, 4.7, title, color, CARD_BG)
        tb_st = slide12.shapes.add_textbox(Inches(left + 0.2), Inches(2.8), Inches(3.333), Inches(3.8))
        tf_st = tb_st.text_frame
        tf_st.word_wrap = True
        
        p = tf_st.paragraphs[0]
        p.text = desc
        p.font.name = FONT_BODY
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_BODY
        p.space_after = Pt(12)
        
        if idx == 0:
            add_bullet(tf_st, "Mounting:", "Initial load into <div id='root'>.")
            add_bullet(tf_st, "State Updates:", "Calls to setState / dispatchers.")
        elif idx == 1:
            add_bullet(tf_st, "Pure Functions:", "Components should produce identical output for identical inputs.")
            add_bullet(tf_st, "Tree Calculation:", "Evaluates all child components.")
        else:
            add_bullet(tf_st, "Diff Patching:", "Modifies minimal DOM elements.")
            add_bullet(tf_st, "DOM Painting:", "Browser paints updated pixels.")

    # --------------------------------------------------------------------------
    # SLIDE 13: MODULE 08 (CONT) - DYNAMIC LIST RENDERING & KEYS
    # --------------------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Module 08 (Lists)", "Dynamic List Rendering & The 'key' Prop", "Rendering collections with JavaScript's .map() and why unique keys are mandatory")
    
    add_card(slide13, 0.8, 2.2, 5.7, 4.7, "The Rule of Keys in React Lists", ACCENT_ROSE)
    tb_k1 = slide13.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_k1 = tb_k1.text_frame
    tf_k1.word_wrap = True
    add_bullet(tf_k1, "Why .map() Instead of for Loops:", ".map() transforms an array of data objects into an array of JSX elements that React can render.")
    add_bullet(tf_k1, "What Keys Do:", "Keys give elements a stable identity across renders so React can track additions, removals, and reordering.")
    add_bullet(tf_k1, "The Pitfall of Array Index:", "Using index as a key (key={index}) breaks input focus and component state if items are filtered or sorted.")
    add_bullet(tf_k1, "Golden Rule:", "Always use a unique and permanent identifier from your data (e.g., student.id or rollNo).")

    add_card(slide13, 6.8, 2.2, 5.7, 4.7, "List Rendering Code Example", ACCENT_GREEN)
    code_list = (
        "const students = [\n"
        "  { id: 'S101', name: 'Aarav', dept: 'CSE', gpa: 8.9 },\n"
        "  { id: 'S102', name: 'Fatima', dept: 'IT',  gpa: 9.3 },\n"
        "  { id: 'S103', name: 'Karthik', dept: 'ECE', gpa: 8.1 }\n"
        "];\n\n"
        "export default function StudentTable() {\n"
        "  return (\n"
        "    <table>\n"
        "      <tbody>\n"
        "        {students.map((student) => (\n"
        "          /* Notice mandatory key={student.id} */\n"
        "          <tr key={student.id}>\n"
        "            <td>{student.id}</td>\n"
        "            <td>{student.name}</td>\n"
        "            <td>{student.dept}</td>\n"
        "            <td>{student.gpa}</td>\n"
        "          </tr>\n"
        "        ))}\n"
        "      </tbody>\n"
        "    </table>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide13, 7.05, 2.8, 5.2, 3.8, code_list)

    # --------------------------------------------------------------------------
    # SLIDE 14: MODULE 09 - PRACTICAL STUDENT PROFILE DASHBOARD
    # --------------------------------------------------------------------------
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Module 09 (Hands-on Lab)", "Practical Project: Student Profile Dashboard", "Assembling a responsive, multi-component student dashboard using React & Vite")
    
    add_card(slide14, 0.8, 2.2, 5.7, 4.7, "Component Architecture Breakdown", ACCENT_CYAN)
    tb_d1 = slide14.shapes.add_textbox(Inches(1.05), Inches(2.8), Inches(5.2), Inches(3.8))
    tf_d1 = tb_d1.text_frame
    tf_d1.word_wrap = True
    add_bullet(tf_d1, "App.jsx (Root):", "Top-level layout importing mock student data and orchestrating child components.")
    add_bullet(tf_d1, "Header.jsx:", "Portal title, branding logo, and navigation indicators.")
    add_bullet(tf_d1, "ProfileCard.jsx:", "Displays student avatar image, full name, roll number, department, and bio.")
    add_bullet(tf_d1, "AcademicStats.jsx:", "CGPA score, semester record, and conditional attendance eligibility tag.")
    add_bullet(tf_d1, "SkillsList.jsx:", "Dynamically maps over technical skills array rendering styled badge components.")
    add_bullet(tf_d1, "ContactCard.jsx:", "Active links for email, phone, GitHub, and LinkedIn profiles.")

    add_card(slide14, 6.8, 2.2, 5.7, 4.7, "Execution & Build Checklist", ACCENT_INDIGO)
    code_dash = (
        "# 1. Initialize Vite project in workspace\n"
        "npm create vite@latest student-dashboard -- --template react\n"
        "cd student-dashboard\n"
        "npm install\n\n"
        "# 2. Component Organization\n"
        "src/\n"
        "  components/\n"
        "    Header.jsx\n"
        "    ProfileCard.jsx\n"
        "    AcademicStats.jsx\n"
        "    SkillsList.jsx\n"
        "    ContactCard.jsx\n"
        "  student-data.js   # Mock profile dataset\n"
        "  App.jsx           # Composition root\n\n"
        "# 3. Run and Verify\n"
        "npm run dev"
    )
    add_code_box(slide14, 7.05, 2.8, 5.2, 3.8, code_dash)

    # --------------------------------------------------------------------------
    # SLIDE 15: MODULE 10 - PLACEMENT TECHNICAL INTERVIEW Q&A
    # --------------------------------------------------------------------------
    slide15 = prs.slides.add_slide(blank_layout)
    add_header(slide15, "Module 10", "Placement Focus: Core Technical Interview Q&A", "Top campus recruitment questions asked by top tech firms and product companies")
    
    questions = [
        ("Q1: Is React a library or framework?", "React is a library. It focuses exclusively on building UI (View layer), providing developers architectural freedom to choose their own router, state store, and build tools."),
        ("Q2: How does the Virtual DOM enhance performance?", "The VDOM avoids costly browser Reflow and Repaint by diffing changes in memory with an O(n) algorithm and batching only necessary updates to the Real DOM."),
        ("Q3: Why can't browsers read JSX directly?", "JSX is not valid ECMAScript. It is syntactic sugar for React.createElement() and must be transpiled by Babel or esbuild before browser execution."),
        ("Q4: Why must component names be PascalCase?", "React uses casing to distinguish between built-in HTML tags (<button>, <div>) and custom React components (<ProfileCard />)."),
        ("Q5: Why is the 'key' prop mandatory in lists?", "Keys provide stable element identity during reconciliation. Without keys, React re-renders the entire list and risks state corruption across items.")
    ]
    
    for idx, (q, a) in enumerate(questions):
        top = 2.2 + idx * 0.95
        card = add_card(slide15, 0.8, top, 11.733, 0.85, None, CARD_BORDER, CARD_BG)
        tb_q = slide15.shapes.add_textbox(Inches(1.05), Inches(top + 0.1), Inches(11.2), Inches(0.65))
        tf_q = tb_q.text_frame
        tf_q.word_wrap = True
        tf_q.margin_left = tf_q.margin_right = tf_q.margin_top = tf_q.margin_bottom = 0
        
        p = tf_q.paragraphs[0]
        run_q = p.add_run()
        run_q.text = q + " "
        run_q.font.name = FONT_HEADING
        run_q.font.bold = True
        run_q.font.size = Pt(11)
        run_q.font.color.rgb = ACCENT_AMBER
        
        run_a = p.add_run()
        run_a.text = a
        run_a.font.name = FONT_BODY
        run_a.font.size = Pt(10)
        run_a.font.color.rgb = TEXT_BODY

    # --------------------------------------------------------------------------
    # SLIDE 16: MODULE 10 (CONT) - LIVE CODING CHALLENGES
    # --------------------------------------------------------------------------
    slide16 = prs.slides.add_slide(blank_layout)
    add_header(slide16, "Module 10 (Coding Drills)", "Placement Focus: Live Coding Challenge Patterns", "Practical coding challenges commonly presented during technical screening rounds")
    
    add_card(slide16, 0.8, 2.2, 5.7, 4.7, "Challenge 1: Bounded Counter with Limits", ACCENT_CYAN)
    code_ch1 = (
        "// Task: Counter with Min: 0, Max: 10 limits\n"
        "function BoundedCounter() {\n"
        "  const [count, setCount] = useState(0);\n\n"
        "  return (\n"
        "    <div>\n"
        "      <p>Count: {count}</p>\n"
        "      <button\n"
        "        onClick={() => setCount(count - 1)}\n"
        "        disabled={count <= 0}\n"
        "      >\n"
        "        - Decrement\n"
        "      </button>\n"
        "      <button\n"
        "        onClick={() => setCount(count + 1)}\n"
        "        disabled={count >= 10}\n"
        "      >\n"
        "        + Increment\n"
        "      </button>\n"
        "    </div>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide16, 1.05, 2.8, 5.2, 3.8, code_ch1)

    add_card(slide16, 6.8, 2.2, 5.7, 4.7, "Challenge 2: Conditional Candidate List", ACCENT_GREEN)
    code_ch2 = (
        "// Task: Render list with conditional status badge\n"
        "function CandidateList({ candidates }) {\n"
        "  return (\n"
        "    <ul>\n"
        "      {candidates.map((c) => (\n"
        "        <li key={c.id}>\n"
        "          <span>{c.name}</span> - \n"
        "          <span className={\n"
        "            c.status === 'Selected' \n"
        "              ? 'badge-success' \n"
        "              : 'badge-pending'\n"
        "          }>\n"
        "            {c.status}\n"
        "          </span>\n"
        "        </li>\n"
        "      ))}\n"
        "    </ul>\n"
        "  );\n"
        "}"
    )
    add_code_box(slide16, 7.05, 2.8, 5.2, 3.8, code_ch2)

    # --------------------------------------------------------------------------
    # SLIDE 17: SUMMARY & CHEAT SHEET
    # --------------------------------------------------------------------------
    slide17 = prs.slides.add_slide(blank_layout)
    add_header(slide17, "Wrap Up", "Core React Concepts Summary & Cheat Sheet", "Essential principles to remember for professional development and placement interviews")
    
    cards_data = [
        ("Declarative UI", "Describe WHAT should be rendered for the current state (UI = f(State)). React handles all DOM updates automatically.", ACCENT_CYAN),
        ("Virtual DOM", "In-memory tree compared using an O(n) diffing algorithm. Only differences are batched to the Real DOM.", ACCENT_INDIGO),
        ("Vite Speed", "Native browser ES Modules + esbuild (Go) yields sub-second dev startup and instant HMR.", ACCENT_GREEN),
        ("JSX Rules", "Must return single root (use Fragments <>), close all tags (<img />), camelCase attributes (className).", ACCENT_AMBER),
        ("Components", "Must use PascalCase (ProfileCard). LEGO-like composition of small, reusable, single-responsibility functions.", ACCENT_ROSE),
        ("List Keys", "Mandatory key prop using stable IDs (not array index) for reliable reconciliation during array mapping.", ACCENT_CYAN)
    ]
    
    for idx, (title, desc, color) in enumerate(cards_data):
        col = idx % 3
        row = idx // 3
        left = 0.8 + col * 4.0
        top = 2.2 + row * 2.3
        
        c = add_card(slide17, left, top, 3.733, 2.1, title, color, CARD_BG)
        tb_sm = slide17.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.7), Inches(3.333), Inches(1.3))
        tf_sm = tb_sm.text_frame
        tf_sm.word_wrap = True
        tf_sm.margin_left = tf_sm.margin_right = tf_sm.margin_top = tf_sm.margin_bottom = 0
        
        p = tf_sm.paragraphs[0]
        p.text = desc
        p.font.name = FONT_BODY
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_BODY

    # Save presentation
    output_path = "e:\\mohammed sathak\\React_and_JSX_Masterclass.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    build_deck()
