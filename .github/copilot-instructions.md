# OctoFit Tracker - AI Agent Guidelines

## Project Overview
OctoFit Tracker is a fitness app for high school students featuring user authentication, activity logging, team management, leaderboards, and personalized suggestions. Built with React frontend, Django REST backend, and MongoDB database.

## Architecture
- **Frontend**: React.js in `octofit-tracker/frontend/`
- **Backend**: Django REST Framework in `octofit-tracker/backend/`
- **Database**: MongoDB via Djongo (Django MongoDB connector)
- **Structure**: Root `octofit-tracker/` contains `backend/` and `frontend/` subdirs

## Key Conventions

### Backend (Django)
- **Settings**: Always include codespace-aware ALLOWED_HOSTS:
  ```python
  import os
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  if os.environ.get('CODESPACE_NAME'):
      ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
  ```
- **Serializers**: Convert MongoDB ObjectId fields to strings for JSON compatibility
- **URLs**: Use codespace environment for base URL in `urls.py`:
  ```python
  codespace_name = os.environ.get('CODESPACE_NAME')
  base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
  ```
- **Database**: Use Django ORM exclusively; avoid direct MongoDB queries/scripts
- **Testing**: Use `curl` for endpoint testing

### Frontend (React)
- **Setup**: Use `npx create-react-app --template cra-template --use-npm`
- **Styling**: Bootstrap CSS imported in `src/index.js`
- **Routing**: React Router DOM for navigation
- **Assets**: App logo at `docs/octofitapp-small.png`

## Development Workflows
- **Environment**: Create venv with `python3 -m venv octofit-tracker/backend/venv`
- **Dependencies**: Activate venv and `pip install -r octofit-tracker/backend/requirements.txt`
- **MongoDB**: Check status with `ps aux | grep mongod`; use Django ORM for all data operations
- **Commands**: Always specify full paths (e.g., `--prefix octofit-tracker/frontend`); never `cd` in scripts
- **Ports**: Backend on 8000 (public), Frontend on 3000 (public), MongoDB on 27017 (private)

## Integration Patterns
- **API Communication**: RESTful endpoints between React frontend and Django backend
- **Data Flow**: Frontend logs activities → Backend validates/stores → Leaderboards calculated server-side
- **Authentication**: Django allauth for user management
- **Cross-Origin**: CORS headers configured for frontend-backend communication

## File References
- Setup instructions: `.github/instructions/octofit_tracker_setup_project.instructions.md`
- Backend guidelines: `.github/instructions/octofit_tracker_django_backend.instructions.md`
- Frontend guidelines: `.github/instructions/octofit_tracker_react_frontend.instructions.md`
- Project story: `docs/octofit_story.md`