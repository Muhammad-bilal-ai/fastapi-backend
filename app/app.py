from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "new post", "content": "new cool text post"},
    2: {"title": "morning vibes", "content": "Starting the day with positive energy!"},
    3: {"title": "tech thoughts", "content": "AI is evolving faster than ever—exciting times!"},
    4: {"title": "daily motivation", "content": "Small progress is still progress. Keep going!"},
    5: {"title": "chill mode", "content": "Taking a break to recharge my mind."},
    6: {"title": "coding life", "content": "Debugging is like being a detective in a crime movie."},
    7: {"title": "random idea", "content": "What if creativity is just structured chaos?"},
    8: {"title": "late night grind", "content": "Working while the world sleeps hits differently."},
    9: {"title": "weekend mood", "content": "Relax, refresh, and reset for the week!"},
    10: {"title": "mindset shift", "content": "Your only competition is who you were yesterday."}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
     text_posts[max(text_posts.keys()) + 1] = {"title": post.title, "content": post.content}
    