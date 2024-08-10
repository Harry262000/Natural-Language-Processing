import streamlit as st
from PIL import Image
import base64
from io import BytesIO  # Import BytesIO from the io module
import os  # Import os for file path checking
import json
from streamlit_calendar import calendar

# Initial page config
st.set_page_config(
     page_title='Streamlit Cheat Sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Load the image for the circular display
image_path = "assets/images/86480339.jpeg"  # Adjust this path as needed
image = Image.open(image_path)

# Load the LinkedIn and GitHub icons
linkedin_icon_path = "assets/icons/linkedin.png"  # Adjust this path as needed
github_icon_path = "assets/icons/github.png"
Resume_icon_path = "assets/icons/approved.png"  # Adjust this path as needed

# Function to load images with error handling
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Image not found: {image_path}")
        return None

linkedin_icon = load_image(linkedin_icon_path)
github_icon = load_image(github_icon_path)
Resume_icon = load_image(Resume_icon_path)

# Convert images to base64 for inline display
def image_to_base64(image):
    if image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

linkedin_icon_base64 = image_to_base64(linkedin_icon)
github_icon_base64 = image_to_base64(github_icon)
Resume_icon_base64 = image_to_base64(Resume_icon)

# Display the image in a circular shape using CSS
st.markdown("""
    <style>
    .circle-image {
        width: 150px;  /* Adjust the size as needed */
        height: 150px; /* Adjust the size as needed */
        border-radius: 50%; /* This makes the image circular */
        overflow: hidden; /* Ensures the image fits within the circle */
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Optional shadow */
        margin: 20px auto; /* Center the image and add space after it */
    }
    .circle-image img {
        width: 100%;
        height: auto; /* Maintain aspect ratio */
        object-fit: cover; /* Cover the div without stretching */
    }
    .sidebar-text {
        text-align: center; /* Center the text */
        margin-bottom: 10px; /* Add space between the lines */
    }
    .sidebar-link {
        text-align: center; /* Center the links */
        margin-bottom: 10px; /* Add space between the links */
    }
    .sidebar-section-title {
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .social-icons img {
        width: 24px; /* Adjust the size as needed */
        height: 24px; /* Adjust the size as needed */
        margin: 0 10px; /* Add space between the icons */
    }
    </style>
""", unsafe_allow_html=True)

# Convert the image to base64 for inline display
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display the circular image in the sidebar
with st.sidebar:
    st.markdown(f'<div class="circle-image"><img src="data:image/jpeg;base64,{img_str}"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Harshal Honde</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Data Science Intern @Nroad</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Pune, IN</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Contact Information: </div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">HarshalHonde50@gmail.com</div>', unsafe_allow_html=True)
    if linkedin_icon_base64 and github_icon_base64:
        st.markdown(f"""
            <div class="social-icons" style="text-align: center;">
                <a href="https://www.linkedin.com/in/harshal-honde268/">
                    <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn">
                </a>
                <a href="https://github.com/Harry262000">
                    <img src="data:image/png;base64,{github_icon_base64}" alt="GitHub">
                </a>
                 <a href="/assets/Resume/Harshal_Honde_Intern.pdf">
                    <img src="data:image/png;base64,{Resume_icon_base64}" alt="Resume">
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Machine Learning</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Data Analysis</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section-title">Hobbies and Interests</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Reading</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Traveling</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Gaming</div>', unsafe_allow_html=True)

# Title 
st.title("Tracking My Impact: Contributions Across Various Open Source Projects")

st.subheader("Who Am I?")
st.write("As a passionate open-source contributor, I focus on impactful projects that drive innovation. Committed to pushing the boundaries of technology, I transform complex challenges into elegant solutions. Explore my journey of exploration and creativity across a diverse range of projects and see how my contributions are making a difference!")

# Define the path to your configuration file
config_file = "app/config.json"

# Load metrics from the configuration file or initialize if not present
if os.path.exists(config_file):
    with open(config_file, "r") as f:
        metrics = json.load(f)
else:
    metrics = {
        "Total issues solved": 100,
        "Total pull requests merged": 50,
        "Projects contributed to": 10,
        "New features added": 20
    }

# Function to save metrics to the configuration file
def save_metrics(metrics):
    with open(config_file, "w") as f:
        json.dump(metrics, f, indent=4)

# Define columns
row1 = st.columns(4)

# Display metrics
for col, (label, value) in zip(row1, metrics.items()):
    with col:
        st.metric(label=label, value=value)

# Password protection
password = st.text_input("Enter admin password to edit metrics:", type="password")

# Show input fields if the correct password is entered
if password == "your_secure_password":
    st.markdown("""
        <style>
        .hidden-input {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # Use hidden number inputs for editing metrics
    for label in metrics.keys():
        with st.expander(f"Edit {label}", expanded=False):
            new_value = st.number_input(
                label,
                value=metrics[label],
                step=1,
                key=label,
                format="%d"
            )
            if new_value != metrics[label]:
                metrics[label] = new_value
                save_metrics(metrics)
                st.success(f"{label} updated successfully!")

# Load existing events from a JSON file
def load_events():
    if os.path.exists('events.json'):
        with open('events.json', 'r') as f:
            return json.load(f)
    return []

# Save events to a JSON file
def save_events(events):
    with open('events.json', 'w') as f:
        json.dump(events, f)

# Load existing events from a JSON file
def load_events():
    if os.path.exists('events.json'):
        with open('events.json', 'r') as f:
            return json.load(f)
    return []

# Save events to a JSON file
def save_events(events):
    with open('events.json', 'w') as f:
        json.dump(events, f)

# Load the events
calendar_events = load_events()

tab1, tab2 = st.tabs(["Calendar view", "Graph view"])

# Content for Tab 1
with tab1:
    calendar_options = {
        "editable": True,
        "selectable": True,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridDay,dayGridWeek,dayGridMonth",
        },
        "slotMinTime": "06:00:00",
        "slotMaxTime": "18:00:00",
        "initialView": "dayGridMonth",
    }
    
    custom_css = """
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """
    
    password = st.text_input("Enter admin password to edit events:", type="password")

    if password == "your_secure_password":
        st.write("You are logged in as admin.")
        st.write("Click on a date to add an event.")
        
        selected_date = st.date_input("Select a date")
        event_title = st.text_input("Event Title")
        event_start = st.time_input("Start Time")
        event_end = st.time_input("End Time")
        
        if st.button("Add Event"):
            new_event = {
                "title": event_title,
                "start": f"{selected_date}T{event_start}",
                "end": f"{selected_date}T{event_end}",
            }
            calendar_events.append(new_event)
            save_events(calendar_events)
            st.success("Event added successfully!")
    
    # Display the calendar without showing the returned data
    calendar_view = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
    st.components.v1.html(calendar_view, height=700)

# Content for Tab 2 (Graph view)
with tab2:
    st.write("Graph view content here")
