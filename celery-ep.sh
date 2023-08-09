#!/bin/sh
celery -A services.app worker -l info & celery -A services.app beat -l info