from builtins import print
from flask import Flask, render_template, request, escape, session, make_response
from website import app, db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from flask import redirect, url_for
from flask import jsonify
import json
from pprint import pprint
from io import StringIO
# from werkzeug.utils import secure_filename


from website.models import Post, User, Category, PostCategory

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))



@app.route('/')
@app.route('/index')  # this function responds to requested                                            given to /index path (decorator)
def index():
    category_list = db.session.query(Category.name).all()

    posts = db.session.query(Post).all()
    for post in posts:
        print(post)
        user = db.session.query(User).filter(User.id == post.user_id).one()
        post.author = user.username
        categories_id = db.session.query(PostCategory.category_id).filter(PostCategory.post_id == post.id).all()
        i = 0
        post.category = {}
        for category_id in categories_id:
            category = db.session.query(Category.name).filter(Category.id == category_id[0]).one()
            post.category[i] = category[0]
            i = i+1


    return render_template('index.html', page_title="پایلاگ", posts = posts, categories = category_list)

@app.route('/home')
def home():
    return render_template('home.html', page_title="صفحه اصلی")

@app.route('/course')
def course():
    return render_template('course.html', page_title="Courses")


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', page_title="پروفایل")

@app.route('/add-news', methods=['GET', 'POST'])
@login_required
def add_news():
    category_list = db.session.query(Category.name).all()

    if request.method == "POST":
        if request.form['submit'] == '' or request.form['submit'] == None:
            print('Not exists')
        else:
            input_request = request.form
            last_post = db.session.query(Post).filter()
            category = db.session.query(Category.id).filter(Category.name == input_request['post_categories']).one()
            input_category_id = category.id
            print(input_category_id)
            if input_category_id == None:
                print('Category Not exists')
            else:
                post = Post(
                    user_id=1,
                    title=input_request['post_title'],
                    content=request.form['post_content'],
                    image_url= 'blog-9.jpg',
                )
                db.session.add(post)
                db.session.commit()

                print('add new post')
                all_post = db.session.query(Post).all()
                last_id = all_post[-1].id
                print('last id success')
                post_category = PostCategory(
                    post_id = last_id,
                    category_id = input_category_id
                )
                db.session.add(post_category)
                db.session.commit()

                print(" دسنه بندی هم ست شد:)")

    return render_template('add-news.html', page_title="افزودن خبر", categories = category_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("hello login")
        if request.form['user_name'] == '' or request.form['user_name'] == None:
            print('Not exist')
            return redirect(url_for('login'))
        if request.form['user_password'] == '' or request.form['user_password'] == None:
            print('Not exist')
            return redirect(url_for(login))
        print("hello")
        user = db.session.query(User).filter_by(username = request.form['user_name']).first()
        print(user)
        print(request.form['user_password'])
        if user is not None and user.check_password(request.form['user_password']) and user.status == 1:
            print("user loged in")
            login_user(user)
            print(current_user)
            return redirect(request.args.get('next') or url_for('home'))

    category_list = db.session.query(Category.name).all()
    return render_template('login.html', page_title="صفحه اصلی", categories = category_list)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("signup loaded")
    if request.method == "POST":
        print("method is post")
        if request.form['user_name'] == '' or request.form['user_name'] == None:
            print('Not exist')
            return redirect(url_for('signup'))
        if request.form['user_password'] == '' or request.form['user_password'] == None:
            print('Not exist')
            return redirect(url_for('signup'))
        if request.form['user_repeat_password'] != request.form['user_password']:
            print("bad request")
            return redirect(url_for('signup'))
        user = User(
            username = request.form['user_name'],
            password = request.form['user_password'],
            email = request.form['user_email']
        )
        print(request.form['user_password'])
        print("user created")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    category_list = db.session.query(Category.name).all()

    return render_template('sign-up.html', page_title="ثبت نام", categories = category_list)

@app.route('/users')
@login_required
def users():
    users = db.session.query(User).all()
    return render_template('users.html', page_title="ویرایش اعضا", users=users)

@app.route('/user/<int:id>')
def user(id):
    single_user = User.query.filter(User.id == id).first()
    print(single_user)
    users_role = {'admin', 'professor', 'student'}
    return render_template('edit-user.html', page_title="کاربر"+str(id), user=single_user, users_role= users_role)

@app.route('/post/<int:post_id>')
def post(post_id):
    category_list = db.session.query(Category.name).all()

    post = db.session.query(Post).filter(Post.id == post_id).one()
    print(post)

    user = db.session.query(User).filter(User.id == post.user_id).one()
    # print(user)
    post.author = user.username
    # print(post.author)

    categories_id = db.session.query(PostCategory.category_id).filter(PostCategory.post_id == post.id).all()
    # print('categories_id: ', categories_id)
    i = 0
    post.category = {}
    for category_id in categories_id:
        category = db.session.query(Category.name).filter(Category.id == category_id[0]).one()
        post.category[i] = category[0]
        # print(post.category[i])
        i = i + 1
    return render_template('post.html', page_title='پست', post=post, categories = category_list)

@app.route('/about')
def about():
    return render_template('about.html', page_title='درباره ما')

@app.route('/category/<string:category_name>')
def category(category_name):
    category_list = db.session.query(Category.name).all()

    category = db.session.query(Category.id).filter(Category.name == category_name).one()
    category_id = category.id

    posts = {}
    posts_id = db.session.query(PostCategory.post_id).filter(PostCategory.category_id == category_id).all()

    i = 0
    for post_id in posts_id:
        # print(post_id[0])
        posts[i] = db.session.query(Post).filter(Post.id == post_id[0]).one()
        i = i+1

    posts = posts.values()
    for post in posts:
        print(post.image_url)

        user = db.session.query(User).filter(User.id == post.user_id).one()
        post.author = user.username

        categories_id = db.session.query(PostCategory.category_id).filter(PostCategory.post_id == post.id).all()

        i = 0
        post.category = {}
        for category_id in categories_id:
            category = db.session.query(Category.name).filter(Category.id == category_id[0]).one()
            post.category[i] = category[0]
            i = i + 1

    print("yes it is good")
    return render_template('category.html', page_title=category_name, posts=posts, categories = category_list)

''' API Section '''

@app.route('/api/v1/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter(User.id == id).first()
    db.session.delete(user)
    db.session.commit()
    if user != None:
        return make_response("", 200)
    else:
        return make_response("", 404)

@app.route('/api/v1/user/<int:id>', methods=["PUT"])
def update_user(id):
    if request.method == "PUT":
        io = StringIO()
        print("get put request!")
        json_data = request.json
        # pprint(json_data["pass"])
        # json_data = json.dumps(json_data)
        # json_data = str(json_data, 'ascii')
        print(json_data)
        data = json.loads(json_data)
        print(data)
    else:
        print("No put request")
    new_candidate = {
        "password": request.form["pass"],
        "status": request.form["status"],
        "role": request.form["role"]
    }
    print(new_candidate["password"])
    user = User.query.filter(User.id == id).first()
    user.password = new_candidate["password"]
    user.status = new_candidate["status"]
    user.user_role = new_candidate["role"]
    db.session.commit()
    if user != None:
        return redirect(url_for('users'))
    else:
        return make_response("", 404)

