# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_scraped', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScrapedCandidate',
            new_name='Candidate',
        ),
        migrations.RenameModel(
            old_name='ScrapedCandidateCommittee',
            new_name='CandidateCommittee',
        ),
        migrations.RenameModel(
            old_name='CandidateScrapedElection',
            new_name='CandidateElection',
        ),
        migrations.RenameModel(
            old_name='ScrapedIncumbent',
            new_name='Incumbent',
        ),
        migrations.RenameModel(
            old_name='IncumbentScrapedElection',
            new_name='IncumbentElection',
        ),
        migrations.RenameModel(
            old_name='ScrapedProposition',
            new_name='Proposition',
        ),
        migrations.RenameModel(
            old_name='ScrapedPropositionCommittee',
            new_name='PropositionCommittee',
        ),
        migrations.RenameModel(
            old_name='PropositionScrapedElection',
            new_name='PropositionElection',
        ),
    ]