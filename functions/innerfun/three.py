{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9fd7ccba-d404-452f-a045-55610f10cb2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Outer Function\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def outer():\n",
    "    print(\"Outer Function\")\n",
    "def inner():\n",
    "    print(\"Inner Function\")\n",
    "    return 100\n",
    "\n",
    "result=outer()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0daa8de3-0750-45ec-802d-c6c9c5ef4722",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "outer function\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "def outer():\n",
    "    print(\"outer function\")\n",
    "def inner():\n",
    "    print(\"Inner function\")\n",
    "    return 200\n",
    "\n",
    "result=outer()\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ecbcac9-b2a2-44c8-aca4-f5f8439903b3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
