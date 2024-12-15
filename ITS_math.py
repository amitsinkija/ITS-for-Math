import tkinter as tk
from tkinter import messagebox
from rdflib import Graph, Namespace
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

# Load the RDF ontology
g = Graph()
try:
    g.parse("shapes.owl")  
except Exception as e:
    print(f"Error loading RDF file: {e}")

# Define the namespace
mathShapes = Namespace("http://webprotege.stanford.edu/Rfx2w7MGqq8dQGsv77u504")

# Function to query the ontology
def query_ontology(shape_type):
    try:
        results = g.query(f"""
            SELECT ?shape ?base ?height ?radius ?sideLength ?area ?perimeter
            WHERE {{
                ?shape a mathShapes:{shape_type} .
                OPTIONAL {{ ?shape mathShapes:base ?base . }}
                OPTIONAL {{ ?shape mathShapes:height ?height . }}
                OPTIONAL {{ ?shape mathShapes:radius ?radius . }}
                OPTIONAL {{ ?shape mathShapes:sideLength ?sideLength . }}
                ?shape mathShapes:area ?area .
                ?shape mathShapes:perimeter ?perimeter .
            }}
        """)
        
        output = ""
        for row in results:
            output += f"Shape: {row.shape}\n"
            if row.base:
                output += f"Base: {row.base}\n"
            if row.height:
                output += f"Height: {row.height}\n"
            if row.radius:
                output += f"Radius: {row.radius}\n"
            if row.sideLength:
                output += f"Side Length: {row.sideLength}\n"
            output += f"Area: {row.area}\n"
            output += f"Perimeter: {row.perimeter}\n\n"
        
        if output == "":
            output = "No data found."
        
        messagebox.showinfo(f"Query Results for {shape_type.capitalize()}", output)
    except Exception as e:
        print(f"Error querying ontology: {e}")
        messagebox.showerror("Query Error", "An error occurred while querying the ontology.")

# Function to show information about triangles
def learn_triangle():
    triangle_window = tk.Toplevel(app)
    triangle_window.title("Learn About Triangles")
    triangle_window.geometry("400x400")
    triangle_window.configure(bg="#f0f0f0")

    info_frame = tk.Frame(triangle_window, bg="#f0f0f0")
    info_frame.pack(pady=20)

    title_label = tk.Label(info_frame, text="Triangles", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title_label.pack()

    # Load and display the local image of a triangle
    triangle_image_path = "Triangle.png" 
    try:
        triangle_img = Image.open(triangle_image_path)
        max_width = 150
        max_height = 100
        triangle_img.thumbnail((max_width, max_height), Image.LANCZOS)
        triangle_photo = ImageTk.PhotoImage(triangle_img)

        img_label = tk.Label(info_frame, image=triangle_photo, bg="#f0f0f0")
        img_label.image = triangle_photo
        img_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading triangle image: {e}")
        messagebox.showerror("Image Error", "Could not load triangle image.")

    description = (
        "Triangles are three-sided polygons. They can be classified as:\n"
        "- Equilateral: All sides are equal.\n"
        "- Isosceles: Two sides are equal.\n"
        "- Scalene: All sides are different.\n\n"
        "Area = (base * height) / 2\n"
        "Perimeter = side1 + side2 + side3"
    )

    description_label = tk.Label(info_frame, text=description, wraplength=350, bg="#f0f0f0", font=("Arial", 12))
    description_label.pack(pady=10)


# Function to show information about circles
def learn_circle():
    circle_window = tk.Toplevel(app)
    circle_window.title("Learn About Circles")
    circle_window.geometry("400x400")
    circle_window.configure(bg="#f0f0f0")

    info_frame = tk.Frame(circle_window, bg="#f0f0f0")
    info_frame.pack(pady=20)

    title_label = tk.Label(info_frame, text="Circles", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title_label.pack()

    circle_image_path = "Circle.png" 
    try:
        circle_img = Image.open(circle_image_path)
        max_width = 150
        max_height = 100
        circle_img.thumbnail((max_width, max_height), Image.LANCZOS)
        circle_photo = ImageTk.PhotoImage(circle_img)

        img_label = tk.Label(info_frame, image=circle_photo, bg="#f0f0f0")
        img_label.image = circle_photo
        img_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading circle image: {e}")
        messagebox.showerror("Image Error", "Could not load circle image.")

    description = (
        "Circles are round shapes with no corners. Key properties include:\n"
        "- Radius: Distance from the center to the edge.\n"
        "- Diameter: Distance across the circle through the center.\n\n"
        "Area = π * (radius^2)\n"
        "Circumference = 2 * π * radius"
    )

    description_label = tk.Label(info_frame, text=description, wraplength=350, bg="#f0f0f0", font=("Arial", 12))
    description_label.pack(pady=10)

# Function to show information about squares
def learn_square():
    square_window = tk.Toplevel(app)
    square_window.title("Learn About Squares")
    square_window.geometry("400x400")
    square_window.configure(bg="#f0f0f0")

    info_frame = tk.Frame(square_window, bg="#f0f0f0")
    info_frame.pack(pady=20)

    title_label = tk.Label(info_frame, text="Squares", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title_label.pack()

    square_image_path = "Square.png"  # Ensure this path is correct
    try:
        square_img = Image.open(square_image_path)
        max_width = 150
        max_height = 100
        square_img.thumbnail((max_width, max_height), Image.LANCZOS)
        square_photo = ImageTk.PhotoImage(square_img)

        img_label = tk.Label(info_frame, image=square_photo, bg="#f0f0f0")
        img_label.image = square_photo  # Keep a reference
        img_label.pack(pady=10)
    except Exception as e:
        print(f"Error loading square image: {e}")
        messagebox.showerror("Image Error", "Could not load square image.")

    description = (
        "Squares are four-sided polygons (quadrilaterals) with all sides equal.\n\n"
        "Area = side * side\n"
        "Perimeter = 4 * side"
    )

    description_label = tk.Label(info_frame, text=description, wraplength=350, bg="#f0f0f0", font=("Arial", 12))
    description_label.pack(pady=10)



# Function to start the quiz
def start_quiz():
    quiz_window = tk.Toplevel(app)
    quiz_window.title("Math Quiz")
    quiz_window.geometry("400x400")
    quiz_window.configure(bg="#f0f0f0")

    score = 0
    question_index = 0

    questions = [
        {
            "question": "What is the area of a triangle with base 10 and height 5?",
            "choices": ["25", "50", "15", "30"],
            "correct_answer": "25"
        },
        {
            "question": "What is the circumference of a circle with radius 7? (Use π ≈ 3.14)",
            "choices": ["43.96", "21.98", "14", "28"],
            "correct_answer": "43.96"
        },
        {
            "question": "What is the area of a square with side length 4?",
            "choices": ["16", "12", "8", "20"],
            "correct_answer": "16"
        },
        {
            "question": " What is the area of a circle with a radius of 10? (Use π ≈ 3.14)",
            "choices": ["314", "200", "150", "100"],
            "correct_answer": "314"
        },
        {
            "question": "What is the perimeter of a square with a side length of 5?",
            "choices": ["20", "25", "15", "30"],
            "correct_answer": "20"
        }
    ]

    def check_answer(selected_choice):
        nonlocal score, question_index
        if selected_choice == questions[question_index]["correct_answer"]:
            score += 1
        question_index += 1
        if question_index < len(questions):
            display_question()
        else:
            display_score_feedback()
            quiz_window.destroy()

    def display_question():
        question_label.config(text=questions[question_index]["question"])
        for i, choice in enumerate(questions[question_index]["choices"]):
            choice_buttons[i].config(text=choice, command=lambda c=choice: check_answer(c))
    
    def display_score_feedback():
        feedback = ""
        if score == len(questions):
            feedback = "Excellent! You got all the answers right!"
        elif score >= len(questions) * 0.8:
            feedback = "Great job! You have a strong understanding of the material."
        elif score >= len(questions) * 0.5:
            feedback = "Good effort! Keep practicing to improve your skills."
        else:
            feedback = "Don't worry! Review the material and try again."

        messagebox.showinfo("Quiz Finished", f"Your score: {score}/{len(questions)}\n\n{feedback}")

    question_label = tk.Label(quiz_window, text="", wraplength=300, bg="#f0f0f0", font=("Arial", 14))
    question_label.pack(pady=20)

    choice_buttons = []
    for _ in range(4):
        btn = tk.Button(quiz_window, text="", command=lambda c="": check_answer(c), bg="#4CAF50", fg="white", font=("Arial", 12))
        btn.pack(pady=5, padx=20, fill=tk.X)
        choice_buttons.append(btn)

    display_question()

# Main application window
app = tk.Tk()
app.title("Intelligent Tutoring System for Math")
app.geometry("700x700")
app.configure(bg="#f0f0f0")

# Header
header = tk.Label(app, text="Intelligent Tutoring System for Math", bg="#f0f0f0", font=("Arial", 24, "bold"))
header.pack(pady=20)

# Learn Section
learn_frame = tk.Frame(app, bg="#f0f0f0")
learn_frame.pack(pady=10)

# Triangle Section
triangle_img = ImageTk.PhotoImage(Image.open(BytesIO(requests.get("https://storage.googleapis.com/a1aa/image/r9LFjfFfdyvEME5bOyKeYTm3VfxrDlJXftLNGJQuZAFbS1WfE.jpg").content)).resize((200, 150)))
triangle_card = tk.Frame(learn_frame, bg="white", relief="raised", bd=2)
triangle_card.grid(row=0, column=0, padx=10, pady=10)
tk.Label(triangle_card, image=triangle_img).pack()
tk.Label(triangle_card, text="Triangles", font=("Arial", 16, "bold")).pack()
tk.Label(triangle_card, text="Learn about different types of triangles, their properties, and how to calculate their area and perimeter.", wraplength=200).pack(pady=5)
tk.Button(triangle_card, text="Let's Learn", command=learn_triangle, bg="#2196F3", fg="white").pack(pady=5)

# Circle Section
circle_img = ImageTk.PhotoImage(Image.open(BytesIO(requests.get("https://storage.googleapis.com/a1aa/image/h5Ze33szedoOwkORrNSq28YE1NeoCmcvJuVuhL3oppygUt1nA.jpg").content)).resize((200, 150)))
circle_card = tk.Frame(learn_frame, bg="white", relief="raised", bd=2)
circle_card.grid(row=0, column=1, padx=10, pady=10)
tk.Label(circle_card, image=circle_img).pack()
tk.Label(circle_card, text="Circles", font=("Arial", 16, "bold")).pack()
tk.Label(circle_card, text="Understand the properties of circles, including radius, diameter, circumference, and area calculations.", wraplength=200).pack(pady=5)
tk.Button(circle_card, text="Let's Learn", command=learn_circle, bg="#2196F3", fg="white").pack(pady=5)

# Square Section
square_image_path = "Square1.png"  # Ensure this path is correct
square_img = ImageTk.PhotoImage(Image.open(square_image_path).resize((200, 150), Image.LANCZOS))
square_card = tk.Frame(learn_frame, bg="white", relief="raised", bd=2)
square_card.grid(row=0, column=2, padx=10, pady=10)
tk.Label(square_card, image=square_img).pack()
tk.Label (square_card, text="Squares", font=("Arial", 16, "bold")).pack()
tk.Label(square_card, text="Explore the properties of squares, including how to calculate their area and perimeter.", wraplength=200).pack(pady=5)
tk.Button(square_card, text="Let's Learn", command=learn_square, bg="#2196F3", fg="white").pack(pady=5)

# Quiz Section
quiz_frame = tk.Frame(app, bg="#f0f0f0")
quiz_frame.pack(pady=20)

btn_quiz = tk.Button(quiz_frame, text="Start General Quiz", command=start_quiz, bg="#FF9800", fg="white", font=("Arial", 14))
btn_quiz.pack(pady=10)

app.mainloop()