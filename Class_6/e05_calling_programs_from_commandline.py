'''Defining Arguments
argparse is a complete argument processing library. Arguments can trigger different actions, specified by the action
argument to add_argument(). Supported actions include storing the argument (singly, or as part of a list), storing a
constant value when the argument is encountered (including special handling for true/false values for Boolean switches),
counting the number of times an argument is seen, and calling a callback to use custom processing instructions.

The default action is to store the argument value. If a type is provided, the value is converted to that type before
it is stored. If the dest argument is provided, the value is saved using that name when the command-line arguments are parsed.

Parsing a Command-Line
After all of the arguments are defined, parse the command-line by passing a sequence of argument strings to parse_args().
 By default, the arguments are taken from sys.argv[1:], but any list of strings can be used. The options are processed
 using the GNU/POSIX syntax, so option and argument values can be mixed in the sequence.

The return value from parse_args() is a Namespace containing the arguments to the command. The object holds the argument
values as attributes, so if the argument's dest is set to "myoption", the value is accessible as args.myoption.'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here",type=str)
parser.add_argument("numero", help="multiplicamos el numero x 2",type=float)
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
print(args.echo)
print(args.numero*2)

