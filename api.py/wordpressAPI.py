try:
    from wordpress_xmlrpc import Client, WordPressPost
    from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
    from wordpress_xmlrpc.methods.users import GetUserInfo

except:
    print(f"Please Install Requirements First `pip install -r requirements.txt`")
    exit()


class Wordpress:
    def __init__(self, link, user, password):
        self.link = link
        self.user = user
        self.password = password
        self.wp = Client(self.link, self.user, self.password)

    def get_all_posts(self):
        return self.wp.call(GetPosts())

    def get_user_info(self):
        return self.wp.call(GetUserInfo())

    def new_post(self, title, content):
        post = WordPressPost()
        post.title = title
        post.content = content
        return self.wp.call(NewPost(post))
