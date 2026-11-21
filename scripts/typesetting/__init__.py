"""The typesetters the projects share, one per family of documents:
accounting, job_hunting and project_management. A project's length script
imports typeset() from the one it needs, e.g.

    from typesetting.job_hunting import typeset

report.py does the work for accounting and project_management, and
job_hunting takes its XML and text helpers from it.
"""
