import requests
import customtkinter as ct

app = ct.CTk()
app.geometry("800x600")
app.title("Targets Modrinth Search")

ask = ct.CTkEntry(app, width=700, placeholder_text="Search")
ask.pack(padx=10, pady=10)

def search():
    url = f"https://api.modrinth.com/v2/search?limit=20&index=relevance&query={ask.get()}"
    response = requests.get(url)
    data = response.json()

    results.delete('1.0', ct.END)
    if "hits" in data:
        for project in data["hits"]:
            results.insert(ct.END, "    " + f"{project['title']}\n    {project['project_type']}\n    {project['author']}\n    ---\n    {project['description']}\n\n")
    else:
        results.insert(ct.END, "No results found\n")

results_frame = ct.CTkFrame(app, width=700, height=400)
results_frame.pack(padx=10, pady=10)

results_scroll = ct.CTkScrollbar(results_frame, width=30, height=10)
results_scroll.pack(side=ct.RIGHT, fill=ct.Y)

results = ct.CTkTextbox(results_frame, width=700, height=400)
results.pack(expand=True, fill=ct.BOTH)

results_scroll.configure(command=results.yview)
results.configure(yscrollcommand=results_scroll.set)

def on_enter(event):
    if event.keysym == 'Return':
        search()

ask.bind('<KeyPress>', on_enter)

app.mainloop()

