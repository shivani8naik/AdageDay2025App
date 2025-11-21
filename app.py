# import os
# from flask import (
#     Flask, render_template, request,
#     redirect, url_for, flash, jsonify
# )
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.secret_key = "adage_day_2025_secret"  # for flash messages

# # ==============================
# # FILE HANDLING CONFIG
# # ==============================
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4", "mov", "webm"}
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# def allowed_file(filename: str) -> bool:
#     """Check if file type is allowed."""
#     return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# # ==============================
# # MAIN EVENT DETAILS
# # ==============================
# EVENT = {
#     "name": "Adage Day 2025",
#     "year": 2025,
#     "tagline": "Celebrating 24 Years of Adage",
#     "dates": "29–30 November 2025"
# }

# # ==============================
# # SCHEDULE
# # ==============================
# SCHEDULE = [
#     {
#         "day_label": "Day 1",
#         "date": "29 November 2025",
#         "title": "Sports Day & Awards Night",
#         "sessions": [
#             {
#                 "time": "07:00 – 09:00",
#                 "title": "Registration & Warm-up",
#                 "location": "Adage Campus Ground",
#                 "details": "Kit collection, badge issue and warm-up sessions.",
#             },
#             {
#                 "time": "09:00 – 12:00",
#                 "title": "Sports Day Events",
#                 "location": "Adage Campus Ground",
#                 "details": "Track & field, team games and fun events.",
#             },
#             {
#                 "time": "12:00 – 13:00",
#                 "title": "Lunch Break",
#                 "location": "Campus Cafeteria",
#                 "details": "Buffet lunch for all participants and families.",
#             },
#             {
#                 "time": "19:00 – 22:00",
#                 "title": "Awards Night",
#                 "location": "Taj Palace – Grand Ballroom",
#                 "details": "Performance awards, long service recognition and entertainment.",
#             },
#         ],
#     },
#     {
#         "day_label": "Day 2",
#         "date": "30 November 2025",
#         "title": "Photoshoot & Gala Night",
#         "sessions": [
#             {
#                 "time": "09:00 – 11:00",
#                 "title": "Team & Department Photoshoot",
#                 "location": "Taj Palace – Lawn Area",
#                 "details": "Group and department photos with professional photographers.",
#             },
#             {
#                 "time": "11:00 – 12:00",
#                 "title": "Brunch Gathering",
#                 "location": "Garden Café",
#                 "details": "Relaxed brunch & informal networking.",
#             },
#             {
#                 "time": "18:30 – 22:30",
#                 "title": "Gala Night",
#                 "location": "Taj Palace – Royal Hall",
#                 "details": "Gala dinner, live music, dance and celebration of 24 years.",
#             },
#         ],
#     },
# ]

# # ==============================
# # CONTACT DIRECTORY
# # ==============================
# CONTACT_CARDS = [
#     {
#         "title": "Event Coordination",
#         "people": [
#             {"name": "Rahul Sharma", "phone": "+91 98211 33445"},
#             {"name": "Priya Mehta", "phone": "+91 98991 44556"},
#         ],
#     },
#     {
#         "title": "Travel & Stay",
#         "people": [
#             {"name": "Alok Gupta", "phone": "+91 75060 39677"},
#             {"name": "Devyani S", "phone": "+91 94038 24212"},
#         ],
#     },
# ]

# # ==============================
# # RULES / GUIDELINES
# # ==============================
# RULES = {
#     "dos": [
#         "Report on time for each event.",
#         "Follow the dress code for Sports Day, Photoshoot and Gala Night.",
#         "Carry your own water bottle.",
#         "Warm up properly before sports events.",
#         "Respect all participants, staff and property.",
#     ],
#     "donts": [
#         "Don’t litter – use the dustbins provided.",
#         "Don’t interrupt ongoing performances or matches.",
#         "Don’t damage venue property or equipment.",
#         "Don’t leave children unattended.",
#     ],
# }

# # ==============================
# # PICKUPS
# # ==============================
# PICKUPS = [
#     {"date": "29-11-2024", "time": "4:15 AM", "pickup": "Hotel Golden Crown", "drop": "Don-Bosco Clg"},
#     {"date": "29-11-2024", "time": "12:00 PM", "pickup": "Don-Bosco Clg", "drop": "Hotel Golden Crown"},
#     {"date": "29-11-2024", "time": "3:45 PM", "pickup": "Hotel Golden Crown", "drop": "Hotel Nanutel"},
#     {"date": "29-11-2024", "time": "11:00 PM", "pickup": "Hotel Nanutel", "drop": "Hotel Golden Crown"},
#     {"date": "30-11-2024", "time": "5:45 AM", "pickup": "Hotel Golden Crown", "drop": "Adage Unit-3 (Verna)"},
#     {"date": "30-11-2024", "time": "7:30 AM", "pickup": "Adage Unit-3 (Verna)", "drop": "Adage Unit-1 (Verna)"},
#     {"date": "30-11-2024", "time": "10:00 AM", "pickup": "Adage Unit-1 (Verna)", "drop": "Hotel Golden Crown"},
#     {"date": "30-11-2024", "time": "4:15 PM", "pickup": "Hotel Golden Crown", "drop": "Adage Unit-2 (Verna)"},
#     {"date": "01-12-2024", "time": "12:30 AM", "pickup": "Adage Unit-2 (Verna)", "drop": "Hotel Golden Crown"},
# ]


# # ==============================
# # ANNOUNCEMENTS
# # ==============================
# ANNOUNCEMENTS = [
#     {
#         "title": "Welcome to Adage Day 2025",
#         "text": "Sports Day reporting begins at 7:00 AM at the Adage Campus Ground.",
#         "tag": "Info",
#         "time": "10 Nov 2025, 09:00 AM"
#     },
#     {
#         "title": "Awards Night Dress Code",
#         "text": "Formal / ethnic evening wear is recommended for the Awards Night.",
#         "tag": "Important",
#         "time": "11 Nov 2025, 04:30 PM"
#     },
#     {
#         "title": "Photoshoot Reminder",
#         "text": "Please assemble with your department by 8:45 AM on Day 2 at the Taj Lawn.",
#         "tag": "Reminder",
#         "time": "12 Nov 2025, 08:15 AM"
#     },
# ]

# # API endpoint for real-time announcements
# @app.route("/api/announcements")
# def announcements_api():
#     return jsonify(ANNOUNCEMENTS)


# # ==============================
# # GALLERY ALBUMS
# # ==============================
# GALLERY_IMAGES = {
#     "Sports Day": "sports",
#     "Awards Night": "awards",
#     "Photoshoot": "photoshoot",
#     "Gala Night": "gala",
# }

# # ==============================
# # ROUTES
# # ==============================
# @app.route("/")
# def home():
#     return render_template(
#         "home.html",
#         event=EVENT,
#         announcements=ANNOUNCEMENTS,
#         schedule=SCHEDULE,
#         active_page="home",
#     )


# @app.route("/message")
# def message():
#     return render_template("message.html", event=EVENT, active_page="message")


# @app.route("/schedule")
# def schedule_page():
#     return render_template(
#         "schedule.html", event=EVENT, schedule=SCHEDULE, active_page="schedule"
#     )


# @app.route("/rules")
# def rules_page():
#     return render_template(
#         "rules.html", event=EVENT, rules=RULES, active_page="rules"
#     )


# @app.route("/contacts")
# def contacts_page():
#     return render_template(
#         "contacts.html", event=EVENT, cards=CONTACT_CARDS, active_page="contacts"
#     )


# @app.route("/announcements")
# def announcements_page():
#     return render_template(
#         "announcements.html",
#         event=EVENT,
#         announcements=ANNOUNCEMENTS,
#         active_page="announcements",
#     )


# @app.route("/gallery")
# def gallery_page():
#     """Display albums with images/videos dynamically loaded."""
#     album = {}
#     for event_name, folder in GALLERY_IMAGES.items():
#         folder_path = os.path.join(app.config["UPLOAD_FOLDER"], folder)
#         os.makedirs(folder_path, exist_ok=True)

#         files = [
#             url_for("static", filename=f"uploads/{folder}/{file}")
#             for file in os.listdir(folder_path)
#             if allowed_file(file)
#         ]

#         album[event_name] = sorted(files, reverse=True)

#     return render_template(
#         "gallery.html", album=album, event=EVENT, active_page="gallery"
#     )

# # @app.route("/guest")
# # def guest_page():
# #     return render_template("guest.html", event=EVENT, active_page="guest")

# @app.route("/guest")
# def guest_page():
#     return render_template("guest.html", event=EVENT, pickups=PICKUPS, active_page="guest")
# # ==============================
# # RUN APP
# # ==============================
# if __name__ == "__main__":
#     app.run(debug=True)




import os
from flask import (
    Flask, render_template, request,
    redirect, url_for, flash, jsonify
)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "adage_day_2025_secret"  # for flash messages


# ==============================
# FILE HANDLING CONFIG
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4", "mov", "webm"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename: str) -> bool:
    """Check if file type is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ==============================
# MAIN EVENT DETAILS
# ==============================
EVENT = {
    "name": "Adage Day 2025",
    "year": 2025,
    "tagline": "Celebrating 24 Years of Adage",
    "dates": "29–30 November 2025",  # <-- FIXED (comma added)
}


# ==============================
# EVENT SCHEDULE
# ==============================
SCHEDULE = [
    {
        "day_label": "Day 1",
        "date": "29 November 2025",
        "title": "Sports Day & Awards Night",
        "sessions": [
            {
                "time": "07:00 – 09:00",
                "title": "Registration & Warm-up",
                "location": "Adage Campus Ground",
                "details": "Kit collection, badge issue and warm-up sessions.",
                "reporting_time": "06:45 AM",
                "dress_code": "Tracksuit / Sportswear",
            },
            {
                "time": "09:00 – 12:00",
                "title": "Sports Day Events",
                "location": "Adage Campus Ground",
                "details": "Track & field, team games and fun events for all.",
                "reporting_time": "08:30 AM",
                "dress_code": "Sports Jersey / Sports Shoes",
            },
            {
                "time": "12:00 – 13:00",
                "title": "Lunch Break",
                "location": "Campus Cafeteria",
                "details": "Buffet lunch for all participants and families.",
                "reporting_time": "-",
                "dress_code": "-",
            },
            {
                "time": "19:00 – 22:00",
                "title": "Awards Night",
                "location": "Taj Palace – Grand Ballroom",
                "details": "Performance awards, long service recognition and entertainment.",
                "reporting_time": "06:30 PM",
                "dress_code": "Formal / Ethnic Evening Wear",
            },
        ],
    },
    {
        "day_label": "Day 2",
        "date": "30 November 2025",
        "title": "Photoshoot & Gala Night",
        "sessions": [
            {
                "time": "09:00 – 11:00",
                "title": "Team & Department Photoshoot",
                "location": "Taj Palace – Lawn Area",
                "details": "Group and department photos with professional photographers.",
                "reporting_time": "08:00 AM",
                "dress_code": "Company T-Shirt & Blue Denims",
            },
            {
                "time": "11:00 – 12:00",
                "title": "Brunch Gathering",
                "location": "Garden Café",
                "details": "Relaxed brunch & informal networking.",
                "reporting_time": "-",
                "dress_code": "-",
            },
            {
                "time": "18:30 – 22:30",
                "title": "Gala Night",
                "location": "Taj Palace – Royal Hall",
                "details": "Gala dinner, live music, dance and celebration.",
                "reporting_time": "06:00 PM",
                "dress_code": "Western / Party Wear",
            },
        ],
    },
]

# ==============================
# GUEST PICKUP / DROP DETAILS
# ==============================
PICKUPS = [
    {"date": "29-11-2024", "time": "4:15 AM", "pickup": "Hotel Golden Crown", "drop": "Don-Bosco Clg"},
    {"date": "29-11-2024", "time": "12:00 PM", "pickup": "Don-Bosco Clg", "drop": "Hotel Golden Crown"},
    {"date": "29-11-2024", "time": "3:45 PM", "pickup": "Hotel Golden Crown", "drop": "Hotel Nanutel"},
    {"date": "29-11-2024", "time": "11:00 PM", "pickup": "Hotel Nanutel", "drop": "Hotel Golden Crown"},
    {"date": "30-11-2024", "time": "5:45 AM", "pickup": "Hotel Golden Crown", "drop": "Adage Unit-3 (Verna)"},
    {"date": "30-11-2024", "time": "7:30 AM", "pickup": "Adage Unit-3 (Verna)", "drop": "Adage Unit-1 (Verna)"},
    {"date": "30-11-2024", "time": "10:00 AM", "pickup": "Adage Unit-1 (Verna)", "drop": "Hotel Golden Crown"},
    {"date": "30-11-2024", "time": "4:15 PM", "pickup": "Hotel Golden Crown", "drop": "Adage Unit-2 (Verna)"},
    {"date": "01-12-2024", "time": "12:30 AM", "pickup": "Adage Unit-2 (Verna)", "drop": "Hotel Golden Crown"},
]


# ==============================
# ANNOUNCEMENTS
# ==============================
ANNOUNCEMENTS = [
    {
        "title": "Welcome to Adage Day 2025",
        "text": "Sports Day reporting begins at 7:00 AM at the Adage Campus Ground.",
        "tag": "Info",
        "time": "10 Nov 2025, 09:00 AM",
    },
    {
        "title": "Awards Night Dress Code",
        "text": "Formal / ethnic evening wear is recommended for the Awards Night.",
        "tag": "Important",
        "time": "11 Nov 2025, 04:30 PM",
    },
    {
        "title": "Photoshoot Reminder",
        "text": "Please assemble with your department by 8:45 AM on Day 2.",
        "tag": "Reminder",
        "time": "12 Nov 2025, 08:15 AM",
    },
]

@app.route("/api/announcements")
def announcements_api():
    return jsonify(ANNOUNCEMENTS)


# ==============================
# GALLERY
# ==============================
GALLERY_IMAGES = {
    "Sports Day": "sports",
    "Awards Night": "awards",
    "Photoshoot": "photoshoot",
    "Gala Night": "gala",
}


# ==============================
# ROUTES
# ==============================
@app.route("/")
def home():
    return render_template(
        "home.html",
        event=EVENT,
        announcements=ANNOUNCEMENTS,
        schedule=SCHEDULE,
        active_page="home",
    )


@app.route("/message")
def message():
    return render_template("message.html", event=EVENT, active_page="message")


@app.route("/schedule")
def schedule_page():
    return render_template("schedule.html", event=EVENT, schedule=SCHEDULE, active_page="schedule")


@app.route("/rules")
def rules_page():
    return render_template("rules.html", event=EVENT, active_page="rules")


@app.route("/contacts")
def contacts_page():
    return render_template("contacts.html", event=EVENT, active_page="contacts")


@app.route("/announcements")
def announcements_page():
    return render_template("announcements.html", event=EVENT, announcements=ANNOUNCEMENTS, active_page="announcements")


@app.route("/guest")
def guest_page():
    return render_template("guest.html", event=EVENT, pickups=PICKUPS, active_page="guest")


@app.route("/gallery")
def gallery_page():
    album = {}
    for event_name, folder in GALLERY_IMAGES.items():
        folder_path = os.path.join(app.config["UPLOAD_FOLDER"], folder)
        os.makedirs(folder_path, exist_ok=True)

        files = [
            url_for("static", filename=f"uploads/{folder}/{file}")
            for file in os.listdir(folder_path)
            if allowed_file(file)
        ]
        album[event_name] = sorted(files, reverse=True)

    return render_template("gallery.html", album=album, event=EVENT, active_page="gallery")


@app.route('/service-worker.js')
def service_worker():
    return app.send_static_file('service-worker.js')

# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
