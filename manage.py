#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalG.settings")
    try:
        from django.core.management import execute_from_command_line
    expect ImportError:

        try:
            import django
        expect ImportError(
            "Couldn't import Django."
        )
        rasie
    execute_from_command_line(sys.argv)
