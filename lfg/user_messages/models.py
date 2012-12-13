from django.db import models
from treebeard.al_tree import AL_Node

class UserMessage(AL_Node):

    # Conversation users
    sender = models.ForeignKey('auth.User', related_name="from_user")
    recipient = models.ForeignKey('auth.User', related_name="to_user")

    # For thread nesting
    parent = models.ForeignKey('self', related_name='children_set', null=True, blank=True, db_index=True)

    # Message content
    subject = models.CharField(max_length=250, null=True)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now=True, null=True)

    # Conversation order
    node_order_by = ['date_sent']

    def __str__(self):
        return "%s -> %s: %s" % (self.sender.username, self.recipient.username, self.subject)

    def __unicode__(self):
        return self.__str__()