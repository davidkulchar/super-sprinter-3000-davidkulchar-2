from flask import Flask, request, render_template, redirect, url_for
from user_story import *

app = Flask(__name__)

@app.route('/list')
def show_user_stories():
    entries = UserStory.select().order_by(UserStory.id.asc())
    return render_template('list.html', entries=entries)

@app.route('/process', methods=['POST'])
def new_us():
    title=request.form['title']
    story_text=request.form['story_text']
    acceptance_criteria=request.form['acceptance_criteria']
    buisness_value=request.form['buisness_value']
    estimation=request.form['estimation']
    status=request.form['status']
    us = UserStory.create(title=title, story_text=story_text, acceptance_criteria=acceptance_criteria, buisness_value=buisness_value, estimation=estimation, status=status)
    us.save()
    return redirect(url_for('show_user_stories'))

@app.route('/')
def index_page():
    return redirect(url_for('show_user_stories'))

@app.route('/update', methods=['POST', 'GET'])
def update_us():
    title = request.form['title']
    story_text = request.form['story_text']
    acceptance_criteria = request.form['acceptance_criteria']
    buisness_value = request.form['buisness_value']
    estimation = request.form['estimation']
    status = request.form['status']
    id = request.form['id']
    query =UserStory.update(title=title,
                    story_text=story_text,
                    acceptance_criteria=acceptance_criteria,
                    buisness_value=buisness_value,
                    estimation=estimation,
                    status=status).where(UserStory.id == id)
    query.execute()
    return redirect(url_for('show_user_stories'))

@app.route('/story/<story_id>', methods=['GET'])
def edit_us(story_id):
    story = UserStory.select().where(UserStory.id==story_id).first()
    if story==None:
        return redirect(url_for('show_user_stories'))
    else:
        return render_template('form_filled.html', story=story)

@app.route('/delete/<story_id>', methods=['GET'])
def delete(story_id):
    story = UserStory.get(UserStory.id==story_id)
    if story==None:
        return redirect(url_for('show_user_stories'))
    else:
        story.delete_instance()
        return redirect(url_for('show_user_stories'))

@app.route('/story', methods=['POST', 'GET'])
def render_form():
    return render_template('form_clear.html')

if __name__ == '__main__':
    app.run()
