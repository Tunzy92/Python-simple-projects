from user import User
from post import Post

app_user_one = User("tunde@gmail.com", "Onabanjo Tunde", "pwd1", "Devops Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("today is going to be a great day", app_user_one.name)
new_post.get_post_info()

