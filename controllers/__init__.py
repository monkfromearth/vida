''' Adds the parent module to current path, sharing between all Python files in this directory'''
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))