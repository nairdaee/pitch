from . import main
from flask import render_template
from ..models import Pitch, Comment, User, Upvote, Downvote
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Pitch Black'
    return render_template('index.html' , title = title)

@main.route('/<cat>', methods=['GET', 'POST'])
def pickup(cat):
    cat = cat
    pitches = Pitch.query.filter_by(category=cat).order_by(Pitch.posted_p.desc()).all()
    return render_template('category.html', pitches=pitches)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id=Pitch.id)

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        user_p = current_user
        category = form.category.data

        new_pitch = Pitch(user_p=current_user._get_current_object().id, title=title, category=category, description = description)

        new_pitch.save_pitch()
        pitches = Pitch.query.filter_by(category=category).order_by(Pitch.posted_p.desc()).all()
        return render_template('category.html', pitches=pitches)
    return render_template('new_pitch.html', form=form)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_comment = Comment(comment=comment,user_c=current_user._get_current_object().id, pitch_id=pitch_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',pitch_id = pitch_id ))

    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('comment.html', form=form, comments=all_comments, pitch=pitch)

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods=['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id=pitch_id)
    pitches = Pitch.query.filter_by(category=pitch.category).order_by(Pitch.posted_p.desc()).all()

    if Upvote.query.filter(Upvote.user_id == user.id, Upvote.pitch_id == pitch_id).first():
        return render_template('category.html', pitches=pitches)

    new_upvote = Upvote(pitch_id=pitch_id, user=current_user)
    new_upvote.save_upvotes()
    
    return render_template('category.html', pitches=pitches)


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods=['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id=pitch_id)
    pitches = Pitch.query.filter_by(category=pitch.category).order_by(Pitch.posted_p.desc()).all()

    if Downvote.query.filter(Downvote.user_id == user.id, Downvote.pitch_id == pitch_id).first():
        return render_template('category.html', pitches=pitches)

    new_downvote = Downvote(pitch_id=pitch_id, user=current_user)
    new_downvote.save_downvotes()
    return render_template('category.html', pitches=pitches)

@main.route('/mypitches', methods=['GET', 'POST'])
@login_required
def my_pitches():
    user = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(user_p=user)
    return render_template('category.html', pitches=pitches)
    

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files: 
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))