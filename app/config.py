import os


PROJECT_ROOT_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


submission_folder = os.path.join(PROJECT_ROOT_PATH, "submission")
if not os.path.exists(submission_folder):
    os.mkdir(submission_folder)
