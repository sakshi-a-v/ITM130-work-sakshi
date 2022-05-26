'''Assignment 2
This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 10 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-2-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
    if from_member in social_graph[to_member]['following']: 
        if to_member in social_graph[from_member]['following']:
            return "friends"
        else:
            return "follower"
        elif to_member in social_graph[from_member]['following']:
            return "followed by"
        else:
            return "no relationship"
    
    print(relationship_status("@jobenilagan","joeilagan",social_graph)) #friends 
