#!/usr/bin/python

import os
import sys
import argparse
import yaml
from lib.validators import *

class Tutorial:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        (self.lesson_key, self.step) = self.parse_state()
        self.lesson = self.get_lesson()

    def get_lesson(self):
        with open(os.path.join(self.base_dir, 'lessons', self.lesson_key)) as lessonfile:
            lesson = yaml.load(lessonfile.read())
        return lesson

    def parse_state(self):
        with open(os.path.join(self.base_dir, '.state'), "r") as statefile:
            state = statefile.read().split(":")
        state[1] = int(state[1])
        return state

    def save_state(self):
        with open(os.path.join(self.base_dir, '.state'), "w") as statefile:
            statefile.write(self.lesson_key + ":" + str(self.step))

    def next_step(self):
        self.step += 1
        self.save_state()

    def get_current_step(self, offset=0):
        if self.step + offset < 0:
            return {'task': 'You have just started the %s lesson.' % self.lesson['title']}

        if self.step + offset > len(self.lesson['steps']) - 1:
            self.step -= 1
            return {'task': 'You just finished the %s lesson.' % self.lesson['title']}

        return self.lesson['steps'][self.step + offset]

    def print_progress(self):
        print("%s [%i/%i]" % (self.lesson['title'], self.step + 1, len(self.lesson['steps'])))

    def get_lessons(self):
        lessons_dir = os.path.join(self.base_dir, 'lessons')
        lessons = []
        for f in os.listdir(lessons_dir):
            with open(os.path.join(lessons_dir, f)) as lessonfile:
                lesson_data = yaml.load(lessonfile.read())
                lesson_data['key'] = f
                lessons.append(lesson_data)

        return lessons


def next_i(args, tut):
    tut.print_progress()
    result = tut.get_current_step()
    print(result['task'])
    do_step = True
    if ('validator' in result):
        validator = eval(tut.lesson_key)()
        method = getattr(validator, result['validator'])
        do_step = method()

    if do_step:
        tut.next_step()

def repeat_i(args, tut):
    tut.print_progress()
    print (tut.get_current_step(offset=-1)['task'])


def show_lessons(args, tut):
    lessons = tut.get_lessons()
    for lesson_data in lessons:
        print("%s: %s" % (lesson_data['title'], lesson_data['description']))

def set_lesson(args, tut):
    lessons = tut.get_lessons()
    for i in lessons:
        if args.lesson.lower() == i['title'].lower():
            tut.lesson_key = i['key']
            tut.step = 0
            tut.save_state()
            print ("Changed lesson to: " + i['title'])
            return

    print("Please pick one of the following lessons (case insensitive):")
    for i in lessons:
        print(i['title'])

def main():
    tut = Tutorial()

    parser = argparse.ArgumentParser(description='Tutorial manager')
    subparsers = parser.add_subparsers(help="Tutorial options")

    p_next = subparsers.add_parser('next', help="Move on to the next step in the tutorial")
    p_next.set_defaults(func=next_i)

    p_current = subparsers.add_parser('repeat', help="Repeat the previous step")
    p_current.set_defaults(func=repeat_i)

    p_lessons = subparsers.add_parser('lessons', help="Show a list of available lessons")
    p_lessons.set_defaults(func=show_lessons)

    p_set_lesson = subparsers.add_parser('set-lesson', help="Pick a lesson to start")
    p_set_lesson.add_argument('lesson')
    p_set_lesson.set_defaults(func=set_lesson)

    if len(sys.argv) == 1:
        args = parser.parse_args(['next'])
    else:
        args = parser.parse_args()
    args.func(args, tut)


main()
