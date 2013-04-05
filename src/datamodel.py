#Database models used in Wikitheoria
#Note: Organization of these classes is important for ReferenceProperty() to function

#TODO: add (indexed=False) to a lot of these.

from google.appengine.ext import db

class Counter(db.Model):
    name = db.StringProperty()
    count = db.IntegerProperty()

#defines a WikiUser object for the datastore
class WikiUser(db.Model):
    alias = db.StringProperty(required=True)
    user_name = db.StringProperty(required=True)
    email = db.EmailProperty()
    real_name = db.StringProperty()
    location = db.StringProperty()
    admin = db.BooleanProperty()
    organization = db.StringProperty()
    birthday = db.DateTimeProperty()
    about = db.StringProperty()
    user_id = db.StringProperty()
    user_object = db.UserProperty(auto_current_user=True)
    join_date = db.DateProperty(auto_now_add=True)
    uid = db.IntegerProperty(required=True)
    
class Article(db.Model):
    title = db.StringProperty()
    author = db.ReferenceProperty(WikiUser)
    date_pub = db.DateTimeProperty(auto_now_add=True)
    markdown = db.TextProperty()
    body = db.TextProperty()
    uid = db.IntegerProperty()
    
class Module(db.Model):
    meta_theory = db.TextProperty()
    theoryMarkdown = db.TextProperty()
    theoryHtml = db.TextProperty()
    scope = db.StringListProperty()
    propositions = db.StringListProperty()
    discipline = db.StringProperty(choices = ('Sociology', 'Psychology', 'Political Science'))
    date_submitted = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    version = db.IntegerProperty()
    title = db.StringProperty()
    contributor = db.ReferenceProperty(WikiUser)
    editors = db.ListProperty(db.Key)
    uid = db.IntegerProperty()
    published = db.BooleanProperty()
    current = db.BooleanProperty()

class VersionCounter(db.Model):
    module = db.IntegerProperty()
    count = db.IntegerProperty()

class ModuleVersion(db.Model):
    module = db.ReferenceProperty(Module)
    version = db.IntegerProperty()
    meta_theory = db.TextProperty()
    scope = db.StringListProperty()
    propositions = db.StringListProperty()
    discipline = db.StringProperty(choices = ('Sociology', 'Psychology', 'Political Science'))
    date_submitted = db.DateTimeProperty(auto_now_add=True)
    title = db.StringProperty()
    contributor = db.ReferenceProperty(WikiUser)

#One Term to many TermDefinitions
class Term(db.Model):
    word = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    popularity = db.IntegerProperty()
    date_submitted = db.DateTimeProperty(auto_now_add=True)
    contributor = db.ReferenceProperty(WikiUser)
    uid = db.IntegerProperty()
    
#Many TermDefinitions to one Term
class TermDefinition(db.Model):
    term = db.ReferenceProperty(Term)
    definition = db.StringProperty()
    function = db.StringProperty(choices = ('noun', 'verb', 'pronoun', 'adjective', 'adverb', 'preposition', 'conjunction', 'interjection', 
                                            'nounPhrase', 'verbPhrase', 'prepositionalPhase', 'adjectivalPhrase', 'adverbialPhrase'))
    popularity = db.IntegerProperty()
    discipline = db.StringProperty()
    date_defined = db.DateTimeProperty(auto_now_add=True)
    contributor = db.ReferenceProperty(WikiUser)
    uid = db.IntegerProperty()
    
#Describes the terms for particular modules
class ModuleTerm(db.Model):
    module = db.ReferenceProperty(Module)
    term = db.ReferenceProperty(Term)
    definition = db.ReferenceProperty(TermDefinition)
    abbreviation = db.StringProperty()

class ArticleComment(db.Model):
    uid = db.IntegerProperty()
    user = db.ReferenceProperty(WikiUser)
    article = db.ReferenceProperty(Article)
    comment = db.TextProperty()
    comment_date = db.DateTimeProperty(auto_now_add=True)

class ModuleComment(db.Model):
    uid = db.IntegerProperty()
    user = db.ReferenceProperty(WikiUser)
    module = db.ReferenceProperty(Module)
    comment = db.TextProperty()
    comment_date = db.DateTimeProperty(auto_now_add=True)

class NotifyFeedbackUser(db.Model):
    user = db.StringProperty()
    email = db.StringProperty()
    
class FeaturedArticle(db.Model):
    article = db.ReferenceProperty(Article)
    featured_date = db.DateTimeProperty(auto_now_add=True)

class FeaturedModule(db.Model):
    module = db.ReferenceProperty(Module)
    featured_date = db.DateTimeProperty(auto_now_add=True)

class AdministratorUser(db.Model):
    user = db.ReferenceProperty(WikiUser)
    
class ContributingUser(db.Model):
    user = db.ReferenceProperty(WikiUser)
    
class ApiKey(db.Model):
    hash = db.StringProperty()
    creationTime = db.TimeProperty()
    user = db.ReferenceProperty(WikiUser)
    nonce = db.IntegerProperty()
    locked = db.BooleanProperty()
    
class ApiHitTimer(db.Model):
    apiKey = db.ReferenceProperty(ApiKey)
    count = db.IntegerProperty()
    timeStamp = db.TimeProperty()
    