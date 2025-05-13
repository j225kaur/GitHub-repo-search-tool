# 🔍 GitHub Repo Search Tool

The GitHub Repo Search Tool is a web-based application built with **Flask** and **Bootstrap** that allows users to search GitHub repositories by keyword, view key metadata (stars, forks, descriptions), and save selected repositories as favorites.

---

## 🌟 Features

- 🔎 **Search GitHub Repos**: Enter a keyword/topic to retrieve the top 10 most-starred repositories.
- 📊 **View Metadata**: See repository stars, forks, and descriptions in a clean UI.
- ❤️ **Save Favorites**: Add selected repositories to your favorites and persist them to a local JSON file.
- ⚡ **Interactive Frontend**: Built with Bootstrap and JavaScript for a smooth user experience.

---

## 🖥️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **API**: GitHub Search API
- **Data Storage**: JSON File (for saved favorites)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/github-repo-search-tool.git
cd github-repo-search-tool
```

### 2. Clone the Repository
```bash
python3 -m venv env_name
source env_name/bin/activate  # On Windows: .\env_name\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask requests
```

### 4. Run the app
```bash
python app.py
```
## Example Usage
Enter a search term (e.g., "machine learning").

View the top 10 repositories sorted by stars.

Click “Add to Favorites” for any repo you'd like to keep.

Click “Save Favorites” to persist them into favorites.json.

## Developed by Jasvin Kaur
Let’s connect on [LinkedIN](https://www.linkedin.com/in/jasvin-kaur/)
