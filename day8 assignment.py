{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# file handling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cannot read the file\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    file=open(\"day2.txt\",\"r\")\n",
    "    file.write(\"hey how are you\")\n",
    "except IOError:\n",
    "    print(\"cannot read the file\")\n",
    "else:\n",
    "    print(\"write ooperation is performed succesfully\")\n",
    "    file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# decorators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, this is before function execution\n",
      "This is inside the function !!\n",
      "This is after function execution\n"
     ]
    }
   ],
   "source": [
    "def hello_decorator(func):\n",
    "    def inner1(): \n",
    "        print(\"Hello, this is before function execution\") \n",
    "        func() \n",
    "  \n",
    "        print(\"This is after function execution\") \n",
    "          \n",
    "    return inner1 \n",
    "   \n",
    "def function_to_be_used(): \n",
    "    print(\"This is inside the function !!\") \n",
    "function_to_be_used = hello_decorator(function_to_be_used)  \n",
    "function_to_be_used()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
