{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e81dcf10",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "edf1a2d3-5263-4972-8078-bd692fde78d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "import datetime as dt\n",
    "from dateutil.relativedelta import relativedelta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "36571e0e-6463-435a-bc77-8b5a134894a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Database\n",
    "engine = create_engine('sqlite:///hawaii.sqlite')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "49b5b849-99d2-46ab-aaef-0bd7fd4ab58c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reflect existing database into a new model\n",
    "Base = automap_base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5dc2d5df-2951-4845-9d41-ca2742995684",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reflect tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f4d6a561-01a9-4126-8d75-db5c9e509bcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save reference to tables\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "c6ca809b-788b-4176-8bed-435eab9b296e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['measurement', 'station']\n"
     ]
    }
   ],
   "source": [
    "print(Base.classes.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "92793e17-5702-46f8-b196-2276c04effac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "0085c845-110c-4912-808c-6bedf47d63f8",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "View function mapping is overwriting an existing endpoint function: testtest",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-72-a640f31f0cd9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Flask routes\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"/\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mdef\u001b[0m \u001b[0mtesttest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;34m\"\"\"Lists all available routes.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     return(\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mdecorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m   1313\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdecorator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1314\u001b[0m             \u001b[0mendpoint\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"endpoint\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1315\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_url_rule\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1316\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mwrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m                 \u001b[1;34m\"before the application starts serving requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m             )\n\u001b[1;32m---> 98\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mupdate_wrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrapper_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36madd_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m   1280\u001b[0m             \u001b[0mold_func\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mview_functions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mendpoint\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1281\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mview_func\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1282\u001b[1;33m                 raise AssertionError(\n\u001b[0m\u001b[0;32m   1283\u001b[0m                     \u001b[1;34m\"View function mapping is overwriting an \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1284\u001b[0m                     \u001b[1;34m\"existing endpoint function: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAssertionError\u001b[0m: View function mapping is overwriting an existing endpoint function: testtest"
     ]
    }
   ],
   "source": [
    "# Flask routes\n",
    "@app.route(\"/\")\n",
    "def testtest():\n",
    "    \"\"\"Lists all available routes.\"\"\"\n",
    "    return(\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/V1.0/precipitation<br/>\"\n",
    "        f\"/api/V1.0/Station<br/>\"\n",
    "        f\"/api/V1.0/tobs<br/>\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "78827033-a4be-4466-ae6d-5d553e287edc",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "View function mapping is overwriting an existing endpoint function: precipitation",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-70-06653385094d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"/api/V1.0/precipitation\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mdef\u001b[0m \u001b[0mprecipitation\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m     \u001b[0mresults\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mMeasurement\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mdecorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m   1313\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdecorator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1314\u001b[0m             \u001b[0mendpoint\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0moptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"endpoint\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1315\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_url_rule\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrule\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1316\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36mwrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     96\u001b[0m                 \u001b[1;34m\"before the application starts serving requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     97\u001b[0m             )\n\u001b[1;32m---> 98\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     99\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    100\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mupdate_wrapper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwrapper_func\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\flask\\app.py\u001b[0m in \u001b[0;36madd_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m   1280\u001b[0m             \u001b[0mold_func\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mview_functions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mendpoint\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1281\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mold_func\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mview_func\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1282\u001b[1;33m                 raise AssertionError(\n\u001b[0m\u001b[0;32m   1283\u001b[0m                     \u001b[1;34m\"View function mapping is overwriting an \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1284\u001b[0m                     \u001b[1;34m\"existing endpoint function: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mendpoint\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAssertionError\u001b[0m: View function mapping is overwriting an existing endpoint function: precipitation"
     ]
    }
   ],
   "source": [
    "@app.route(\"/api/V1.0/precipitation\")\n",
    "def precipitation():\n",
    "    results = session.query(Measurement).all()\n",
    "    session.close()"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
