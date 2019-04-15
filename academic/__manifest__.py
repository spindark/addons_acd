{
"name": "Academic Information System Day",
"version": "1.0",
"depends": [
"base",
"sale",
"board",
],"author": "akhmad.daniel@gmail.com",
"category": "Education",
'website': 'http://www.vitraining.com',
"description": """\
Academic Information System Day1
""",
"data": [
"views/menu.xml",
"views/course.xml",
"views/session.xml",
"views/attendee.xml",
"views/partner.xml",
#"views/workflow.xml",
"security/group.xml",
"security/ir.model.access.csv",
"wizard/create_attendee_view.xml",
"report/session.xml",
#"views/dashboard.xml",

],
"installable": True,
"auto_install": False,
"application": True,
}