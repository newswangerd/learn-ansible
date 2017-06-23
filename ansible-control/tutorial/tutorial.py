#!/usr/bin/python

import os
import sys
import argparse
import yaml
from lessons.validators import *

class Tutorial:

    def __init__(self):
        (self.lesson_key, self.step) = self.parse_state()
        self.lesson = self.get_lesson()

    def get_lesson(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lessons', self.lesson_key + '.yaml')) as lessonfile:
            lesson = yaml.load(lessonfile.read())
        return lesson

    def parse_state(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '.state'), "r") as statefile:
            state = statefile.read().split(":")
        state[1] = int(state[1])
        return state

    def save_state(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '.state'), "w") as statefile:
            statefile.write(self.lesson_key + ":" + str(self.step))

    def next_step(self):
        self.step += 1
        self.save_state()

    def get_current_step(self, offset=0):
        if self.step + offset < 0:
            return {'desc': 'You have just started the %s lesson.' % self.lesson['title']}

        if self.step + offset > len(self.lesson['steps']) - 1:
            return {'desc': 'You just finished the %s lesson.' % self.lesson['title']}

        return self.lesson['steps'][self.step + offset]

def next_i(args, tut):
    result = tut.get_current_step()
    print(result['desc'])
    do_step = True
    if ('validator' in result):
        validator = eval(tut.lesson_key)()
        method = getattr(validator, result['validator'])
        do_step = method()

    if do_step:
        tut.next_step()

def repeat_i(args, tut):
    print (tut.get_current_step(offset=-1)['desc'])


def show_lessons(args, tut):
    for i in tut.lessons:
        print (i)


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

    # p_set_lesson = subparsers.add_parser('set-lesson', help="Pick a lesson to start")
    # p_set_lesson.add_argument('lesson', choices=LESSONS.keys)

    if len(sys.argv) == 1:
        args = parser.parse_args(['next'])
    else:
        args = parser.parse_args()
    args.func(args, tut)


main()
