import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()


@app.get("/items")
def get_items():
    items = [
        {
            "id": 1,
            "title": "Card Layouts",
            "subtitle": "Web Design Techniques",
            "img": "https://via.placeholder.com/512x512.png?text=Card+Layouts",
            "description": "Create visually stunning and interactive card-based layouts for websites. Learn CSS-based techniques including hover effects, 3D transformations, and responsive design."
        },
        {
            "id": 2,
            "title": "Card Designs",
            "subtitle": "Game Development",
            "img": "https://via.placeholder.com/512x512.png?text=Playing+Cards",
            "description": "Develop custom playing card designs using Python. Add text, graphics, and branding elements, with potential applications in game development or digital collectibles."
        },
        {
            "id": 3,
            "title": "Blog Card",
            "subtitle": "Web Design Inspiration",
            "img": "https://via.placeholder.com/512x512.png?text=Blog+Cards",
            "description": "Explore the most creative blog card designs from across the web. Analyze layout styles, typography, and content presentation to enhance blog engagement."
        },
        {
            "id": 4,
            "title": "Microsoft Teams",
            "subtitle": "Teams Platform",
            "img": "https://via.placeholder.com/512x512.png?text=Teams+UI",
            "description": "Discover various card-based UI elements in Microsoft Teams, such as hero cards, thumbnail cards, and adaptive cards. Implement these in custom bots and apps."
        },
        {
            "id": 5,
            "title": "Language Reactor",
            "subtitle": "Language Learning Tools",
            "img": "https://via.placeholder.com/512x512.png?text=Flashcards",
            "description": "Use the Language Reactor extension to generate Anki flashcards from streaming platforms like YouTube. Learn how to import and optimize these cards for language learning."
        },
    ]
    random.shuffle(items)
    return items


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
