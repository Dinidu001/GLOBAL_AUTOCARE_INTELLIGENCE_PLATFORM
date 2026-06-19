import streamlit as st
import urllib.parse
from streamlit_option_menu import option_menu

# Advanced System Configuration
st.set_page_config(
    page_title="Global AutoCare Intelligence Platform", 
    page_icon="⚙️", 
    layout="wide"
)

# Premium Ultra-Modern Cyberpunk & Luxury Automotive Theme
st.markdown("""
    <style>
    /* Global Background & Smooth Scroll */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Main Header Styling */
    .main-title { 
        text-align: center; 
        color: #FF4B4B; 
        font-size: 42px;
        font-weight: 900; 
        margin-bottom: 5px;
        letter-spacing: 2px;
        text-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
    }
    .sub-title { 
        text-align: center; 
        font-size: 14px; 
        color: #38bdf8; 
        margin-bottom: 35px; 
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }
    
    /* Live Matrix Section Header */
    .section-header { 
        color: #38bdf8; 
        border-bottom: 2px solid #0284c7; 
        padding-bottom: 12px; 
        margin-top: 30px;
        font-size: 24px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 📊 Premium Table Design */
    .spec-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin-top: 15px;
        margin-bottom: 30px;
        background-color: #111827;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #1e293b;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .spec-table th {
        background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
        color: #38bdf8;
        text-align: left;
        padding: 16px;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 13px;
        letter-spacing: 0.5px;
        border-bottom: 2px solid #1e293b;
    }
    .spec-table td {
        padding: 16px;
        border-bottom: 1px solid #1e293b;
        font-size: 14px;
        color: #cbd5e1;
    }
    .spec-table tr:last-child td {
        border-bottom: none;
    }
    .spec-table tr:hover {
        background-color: rgba(56, 189, 248, 0.03);
        transition: background-color 0.2s ease;
    }

    /* 🔲 Glassmorphic Form Container */
    div[data-testid="stForm"] {
        border: 1px solid rgba(56, 189, 248, 0.2) !important;
        background: rgba(17, 24, 39, 0.7) !important;
        backdrop-filter: blur(12px);
        padding: 30px !important;
        border-radius: 16px !important;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5) !important;
    }
    
    /* ⌨️ Beautiful Input Fields */
    .stTextInput>div>div>input {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 15px !important;
        transition: all 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0px 0px 10px rgba(56, 189, 248, 0.3) !important;
    }

    /* 🔥 ULTIMATE CENTERED NEON ENTER BUTTON */
    div[data-testid="stForm"] .stButton > button {
        background: linear-gradient(135deg, #FF4B4B 0%, #cb2d3e 100%) !important;
        color: white !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        padding: 12px 40px !important;
        border-radius: 30px !important; /* Rounded Capsule Look */
        border: none !important;
        width: 100% !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0px 5px 15px rgba(255, 75, 75, 0.3) !important;
    }
    div[data-testid="stForm"] .stButton > button:hover {
        background: linear-gradient(135deg, #ff6b6b 0%, #FF4B4B 100%) !important;
        box-shadow: 0px 8px 25px rgba(255, 75, 75, 0.6) !important;
        transform: translateY(-3px) scale(1.03);
    }
    div[data-testid="stForm"] .stButton > button:active {
        transform: translateY(-1px) scale(1);
    }

    /* 🏷️ Navigation Custom Option Menu Adjustments */
    .nav-link-selected {
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4) !important;
    }

    /* 📑 Clean Image Border Radius */
    .stImage>img {
        border-radius: 14px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>⚙️ GLOBAL AUTOCARE INTELLIGENCE PLATFORM</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Master Technical Encyclopedia, Electrical Schematics & Component Topology</p>", unsafe_allow_html=True)

# ==============================================================================
# 🔥 STEP 1: CHOOSE SEARCH METHOD
# ==============================================================================
search_method = option_menu(
    menu_title=None, # හෙඩර් එක අයින් කරලා පෙනුම Clean කරා
    options=["Search by Vehicle Brand & Model", "Search by Chassis / VIN Number"],
    icons=["search", "fingerprint"], 
    menu_icon="layers",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0f172a", "border": "1px solid #1e293b", "border-radius": "10px"}, 
        "icon": {"color": "#38bdf8", "font-size": "15px"}, 
        "nav-link": {"font-size": "14px", "font-weight": "600", "text-align": "center", "color": "#94a3b8", "padding": "10px 0px"},
        "nav-link-selected": {"background-color": "#FF4B4B", "color": "white"},
    }
)
st.write("---")

has_data = False
brand, model, vin_input = "", "", ""

# Input Forms with Premium Centered Enter Button
if search_method == "Search by Vehicle Brand & Model":
    with st.form("vehicle_form"):
        col1, col2 = st.columns(2)
        with col1:
            brand = st.text_input("Enter Vehicle Brand (e.g., Toyota, Honda, BMW):", placeholder="e.g., Toyota").strip().capitalize()
        with col2:
            model = st.text_input("Enter Exact Model Variant (e.g., Corolla, Civic, 320i):", placeholder="e.g., Corolla").strip().capitalize()
        
        st.write("") 
        
        # 🎯 බටන් එක මැදට ගැනීමට Columns 3ක් භාවිත කිරීම
        btn_col1, btn_col2, btn_col3 = st.columns([1.6, 0.8, 1.6])
        with btn_col2:
            submitted = st.form_submit_button("⏎ Enter Matrix")
            
        if submitted and brand and model:
            has_data = True

elif search_method == "Search by Chassis / VIN Number":
    with st.form("vin_form"):
        vin_input = st.text_input("Enter 17-Character Chassis / VIN Number:", placeholder="Enter 17-digit code here...").strip().upper()
        
        st.write("") 
        
        # 🎯 බටන් එක මැදට ගැනීමට Columns 3ක් භාවිත කිරීම
        btn_col1, btn_col2, btn_col3 = st.columns([1.6, 0.8, 1.6])
        with btn_col2:
            submitted = st.form_submit_button("⏎ Enter Matrix")
            
        if submitted and vin_input:
            if len(vin_input) != 17:
                st.error("⚠️ Architectural Error: A standard automotive global VIN identifier must consist of exactly 17 alphanumeric characters.")
            else:
                has_data = True
                brand, model = "Decoded Vehicle", f"({vin_input[0:3]} Series)"

# ==============================================================================
# 🔥 STEP 2: LOAD MASTER COMPONENT TELEMETRY
# ==============================================================================
if has_data:
    st.markdown(f"<h2 class='section-header'>📊 LIVE SYSTEM MATRIX: {brand} {model}</h2>", unsafe_allow_html=True)
    st.write("")
    
    # 📸 DYNAMIC VEHICLE IMAGE ENGINE
    query = urllib.parse.quote(f"{brand} {model} car front")
    st.image(f"https://source.unsplash.com/featured/1200x480/?{query}", caption=f"System Virtual Render Engine Base: {brand} {model}", use_container_width=True)
    st.write("")

    # Master System Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔧 Core Engine & Gearbox",
        "🛞 Chassis & Suspension",
        "⚡ Electrical & Sensors",
        "❄️ A/C & Advanced Filtration",
        "📚 Wiring Schematics"
    ])
    
    # --- TAB 1: CORE ENGINE & TRANSMISSION MAINTENANCE ---
    with tab1:
        st.markdown("<h4 style='color:#38bdf8; font-weight:700;'>💥 Internal Engine Mechanics & Lifespan</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Timing Belt / Chain</b></td><td>Synchronizes crankshaft and camshaft rotation profiles. Steel chains vs high-tensile rubber belts.</td><td><b>Belts:</b> 90,000 km - 100,000 km<br><b>Chains:</b> Inspect at 150,000 km</td></tr>
            <tr><td><b>Spark Plugs</b></td><td>Iridium/Platinum dual core high-intensity spark delivery components.</td><td>Every 60,000 km - 100,000 km</td></tr>
            <tr><td><b>Water Pump</b></td><td>High-flow cooling circulation pump keeping optimal engine thermal state.</td><td>Every 100,000 km (Replace with timing system)</td></tr>
            <tr><td><b>Gaskets & Seals</b></td><td>Engine Valve cover, Main oil seal, and Head gaskets preventing pressure decompression.</td><td>Inspect at 50,000 km (Replace on weeping signs)</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#38bdf8; font-weight:700; margin-top:20px;'>⚙️ Gearbox & Transmission Infrastructure</h4>", unsafe_allow_html=True)
        st.markdown("""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Clutch & Pressure Plates</b></td><td>Friction plates modulating torque between flywheel and pressure mechanism.</td><td>Every 120,000 km - 150,000 km</td></tr>
            <tr><td><b>CV Joints & Axles</b></td><td>Constant Velocity joints transfer dynamic driving force at varying deflection angles.</td><td>Inspect boots every 20,000 km</td></tr>
        </table>
        """, unsafe_allow_html=True)

    # --- TAB 2: CHASSIS, BRAKING & SUSPENSION GEOMETRY ---
    with tab2:
        st.markdown("<h4 style='color:#38bdf8; font-weight:700;'>🛑 Braking Systems & Friction Nodes</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Brake Pads & Rotors</b></td><td>Premium compound pads gripping ventilated cast-iron deceleration discs.</td><td><b>Pads:</b> 30,000 km - 50,000 km<br><b>Rotors:</b> Swap on every 2nd pad change</td></tr>
            <tr><td><b>Wheel Bearings</b></td><td>Double-row sealed angular bearings allowing minimum rolling resistance.</td><td>Replace on road-noise/humming (120,000 km+)</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#38bdf8; font-weight:700; margin-top:20px;'>🛣️ Suspension Geometry & Steering Linkages</h4>", unsafe_allow_html=True)
        st.markdown("""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Shock Absorbers & Bushes</b></td><td>Velocity-sensitive dampers containing high-pressure gas with polyurethane bushings.</td><td>Inspect for fluid leaks every 20,000 km</td></tr>
            <tr><td><b>Ball Joints, Rack Ends & Tie Rods</b></td><td>Multi-axis spherical joints ensuring tracking control and wheel orientation.</td><td>Check on alignment intervals (Replace on slacks)</td></tr>
        </table>
        """, unsafe_allow_html=True)

    # --- TAB 3: ELECTRICAL CONTROLS & MICRO-SENSORS ---
    with tab3:
        st.markdown("<h4 style='color:#38bdf8; font-weight:700;'>🧠 Engine Management Powertrain Sensors</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <table class='spec-table'>
            <tr><th>Sensor Module</th><th>Operational Domain Mapping</th><th>Diagnostic Protocol</th></tr>
            <tr><td><b>Oxygen Sensor (Lambda)</b></td><td>Monitors stoichiometric chemistry post-combustion inside exhaust piping.</td><td>Inspect at 100,000 km (Check P0130 codes)</td></tr>
            <tr><td><b>MAF (Mass Airflow) Sensor</b></td><td>Measures air intake mass index utilizing a heated micro-platinum filament wire.</td><td>Clean with MAF spray every 40,000 km</td></tr>
            <tr><td><b>Camshaft / Crankshaft Sensors</b></td><td>Tracks rotational position indexing for digital injection firing synchronization.</td><td>Replace on crank failure or P0335/P0340 codes</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#38bdf8; font-weight:700; margin-top:20px;'>🔋 Power Alternation & Starter Assemblies</h4>", unsafe_allow_html=True)
        st.markdown("""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Battery</b></td><td>High-cold cranking amp (CCA) EFB/AGM storage cell powering electrical grid.</td><td>2 to 4 Calendar Years</td></tr>
            <tr><td><b>Alternator</b></td><td>Rectified alternator generating current regulated dynamically via LIN-Bus.</td><td>Test brush duty cycle at 150,000 km</td></tr>
            <tr><td><b>Starter Motor</b></td><td>High-torque DC cranking motor with engagement solenoid ring gear.</td><td>Overhaul on slow engine turnover (150,000 km+)</td></tr>
        </table>
        """, unsafe_allow_html=True)

    # --- TAB 4: A/C CLIMATE SYSTEMS & FILTRATION ---
    with tab4:
        st.markdown("<h4 style='color:#38bdf8; font-weight:700;'>❄️ HVAC Thermal Climate Control</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <table class='spec-table'>
            <tr><th>Component Identifier</th><th>Architectural & Technical Description</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>A/C Compressor</b></td><td>Variable displacement scroll compressor compressing refrigerant media.</td><td>Inspect belt clutch annually</td></tr>
            <tr><td><b>Cooling Coil & Condenser</b></td><td>Sub-cooled aluminum heat fin structures exchanging cabin thermal index.</td><td>Clean fins every 20,000 km</td></tr>
            <tr><td><b>Radiator Hoses</b></td><td>Vulcanized EPDM conduits distributing coolant core under pressure.</td><td>Replace every 5 Years or on swelling signs</td></tr>
        </table>
        """, unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#38bdf8; font-weight:700; margin-top:20px;'>🧪 Particulate Matter Filtration Matrix</h4>", unsafe_allow_html=True)
        st.markdown("""
        <table class='spec-table'>
            <tr><th>Filter Media Category</th><th>Functional System Domain</th><th>Overhaul / Replacement Interval</th></tr>
            <tr><td><b>Oil Filter</b></td><td>Traps microscopic micro-wear metallic filings inside engine lubrication lines.</td><td>Change with every oil cycle (10,000 km)</td></tr>
            <tr><td><b>Air & Cabin Filters</b></td><td>Filters combustion intake air stream and cabin HVAC environmental oxygen.</td><td>Every 20,000 km</td></tr>
            <tr><td><b>Fuel Filter</b></td><td>Removes tank sediment elements before reaching high-pressure direct fuel rails.</td><td>Every 40,000 km (In-line) / 100,000 km (In-tank)</td></tr>
        </table>
        """, unsafe_allow_html=True)

    # --- TAB 5: WIRING DIAGRAMS & MANUALS ---
    with tab5:
        st.markdown("### 📚 Factory Documentation Directory")
        wq = f"https://www.google.com/search?q={brand}+{model}+electrical+wiring+diagram+schematic+pdf"
        mq = f"https://www.google.com/search?q={brand}+{model}+factory+service+repair+manual+filetype:pdf"
        st.markdown(f"⚡ **[Access Electrical Wiring Circuit Pinouts for {brand} {model}]({wq})**")
        st.markdown(f"📥 **[Download Master Factory Workshop Manuals for {brand} {model}]({mq})**")

else:
    st.info("💡 Navigation Alert: Please enter the Vehicle details inside the glass frame above and click 'Enter Matrix' to unlock the data streams.")

# ==============================================================================
# 🔥 ENTERPRISE FOOTER WITH YOUR NAME
# ==============================================================================
st.write("---")
st.markdown("<p style='text-align: center; color: #64748b; font-weight: bold;'>Automotive Intelligence System Platform</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>Designed and Developed with Engineering Standards by <span style='color: #FF4B4B; font-weight: bold;'>M.K.D.Sehan</span></p>", unsafe_allow_html=True)