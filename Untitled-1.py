from contextlib import nullcontext
from operator import truediv
from pickle import TRUE


{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "IPL Prediction Model Training.ipynb",
      "provenance": [],
      "toc_visible": truediv,
      "mount_file_id": "1GwVzIXk-E-y7eglc6IlsD8cApR3lrVqh",
      "authorship_tag": "ABX9TyPisIhLe1G5FWLKR2bByNr2",
      "include_colab_link": TRUE
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/thatfreakcoder/IPL-Score-Prediction-with-Machine-Learning/blob/master/IPL_Prediction_Model_Training.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AXBU8kPxT1Al"
      },
      "source": [
        "# IPL 1st Inning Score Prediction using Machine Learning\n",
        "The Dataset contains ball by ball information of the matches played between IPL Teams of **Season 1 to 10**, i.e. from 2008 to 2017.<br/>\n",
        "This Machine Learning model adapts a Regression Appoach to predict the score of the First Inning of an IPL Match.<br/>\n",
        "The Dataset can be downloaded from Kaggle from [here](https://www.kaggle.com/yuvrajdagur/ipl-dataset-season-2008-to-2017).<br/> "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "deQNulMrT_fi"
      },
      "source": [
        "# Import Necessary Libraries\n",
        "and Mounting GDrive for importing Dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p0AuT36T3Eds",
        "outputId": "3e3229fd-f9d4-4aec-ffcf-db49465b6652",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "source": [
        "# Importing Necessary Libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "np.__version__"
      ],
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'1.18.5'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g8WZBYt3wT3t"
      },
      "source": [
        "Mount your Google Drive and save the dataset in the Drive name \"data.csv\""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CHAMX3Kh3LfY",
        "outputId": "1af1fe8b-c599-4326-c150-6c7376956daf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Mounting GDrive and importing dataset\n",
        "data = pd.read_csv('/content/drive/My Drive/data.csv')\n",
        "print(f\"Dataset successfully Imported of Shape : {data.shape}\")"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Dataset successfully Imported of Shape : (76014, 15)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J7CSd3bM4U8S"
      },
      "source": [
        "# Exploratory Data Analysis"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XobBp7D74Pb0",
        "outputId": "32c28941-a7b8-486f-8cc9-8f7a8bf512df",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 306
        }
      },
      "source": [
        "# First 5 Columns Data\n",
        "data.head()"
      ],
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>mid</th>\n",
              "      <th>date</th>\n",
              "      <th>venue</th>\n",
              "      <th>batting_team</th>\n",
              "      <th>bowling_team</th>\n",
              "      <th>batsman</th>\n",
              "      <th>bowler</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>striker</th>\n",
              "      <th>non-striker</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2008-04-18</td>\n",
              "      <td>M Chinnaswamy Stadium</td>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>SC Ganguly</td>\n",
              "      <td>P Kumar</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>2008-04-18</td>\n",
              "      <td>M Chinnaswamy Stadium</td>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>BB McCullum</td>\n",
              "      <td>P Kumar</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>2008-04-18</td>\n",
              "      <td>M Chinnaswamy Stadium</td>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>BB McCullum</td>\n",
              "      <td>P Kumar</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>2008-04-18</td>\n",
              "      <td>M Chinnaswamy Stadium</td>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>BB McCullum</td>\n",
              "      <td>P Kumar</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.3</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>2008-04-18</td>\n",
              "      <td>M Chinnaswamy Stadium</td>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>BB McCullum</td>\n",
              "      <td>P Kumar</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.4</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   mid        date                  venue  ... striker non-striker total\n",
              "0    1  2008-04-18  M Chinnaswamy Stadium  ...       0           0   222\n",
              "1    1  2008-04-18  M Chinnaswamy Stadium  ...       0           0   222\n",
              "2    1  2008-04-18  M Chinnaswamy Stadium  ...       0           0   222\n",
              "3    1  2008-04-18  M Chinnaswamy Stadium  ...       0           0   222\n",
              "4    1  2008-04-18  M Chinnaswamy Stadium  ...       0           0   222\n",
              "\n",
              "[5 rows x 15 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dl5XPiHq4aG0",
        "outputId": "5d833c8a-939a-4760-a972-663ba7038058",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        }
      },
      "source": [
        "# Describing Numerical Values of the Dataset\n",
        "data.describe()"
      ],
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>mid</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>striker</th>\n",
              "      <th>non-striker</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "      <td>76014.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>308.627740</td>\n",
              "      <td>74.889349</td>\n",
              "      <td>2.415844</td>\n",
              "      <td>9.783068</td>\n",
              "      <td>33.216434</td>\n",
              "      <td>1.120307</td>\n",
              "      <td>24.962283</td>\n",
              "      <td>8.869287</td>\n",
              "      <td>160.901452</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>178.156878</td>\n",
              "      <td>48.823327</td>\n",
              "      <td>2.015207</td>\n",
              "      <td>5.772587</td>\n",
              "      <td>14.914174</td>\n",
              "      <td>1.053343</td>\n",
              "      <td>20.079752</td>\n",
              "      <td>10.795742</td>\n",
              "      <td>29.246231</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>67.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>154.000000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.600000</td>\n",
              "      <td>24.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>142.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>308.000000</td>\n",
              "      <td>70.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>9.600000</td>\n",
              "      <td>34.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>20.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>162.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>463.000000</td>\n",
              "      <td>111.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>14.600000</td>\n",
              "      <td>43.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>35.000000</td>\n",
              "      <td>13.000000</td>\n",
              "      <td>181.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>617.000000</td>\n",
              "      <td>263.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>19.600000</td>\n",
              "      <td>113.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>175.000000</td>\n",
              "      <td>109.000000</td>\n",
              "      <td>263.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                mid          runs  ...   non-striker         total\n",
              "count  76014.000000  76014.000000  ...  76014.000000  76014.000000\n",
              "mean     308.627740     74.889349  ...      8.869287    160.901452\n",
              "std      178.156878     48.823327  ...     10.795742     29.246231\n",
              "min        1.000000      0.000000  ...      0.000000     67.000000\n",
              "25%      154.000000     34.000000  ...      1.000000    142.000000\n",
              "50%      308.000000     70.000000  ...      5.000000    162.000000\n",
              "75%      463.000000    111.000000  ...     13.000000    181.000000\n",
              "max      617.000000    263.000000  ...    109.000000    263.000000\n",
              "\n",
              "[8 rows x 9 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mPpXimQR4gCc",
        "outputId": "308fced4-9b9d-45f9-81d6-5f04bf29ab54",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Information (not-null count and data type) About Each Column\n",
        "data.info()"
      ],
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 76014 entries, 0 to 76013\n",
            "Data columns (total 15 columns):\n",
            " #   Column          Non-Null Count  Dtype  \n",
            "---  ------          --------------  -----  \n",
            " 0   mid             76014 non-null  int64  \n",
            " 1   date            76014 non-null  object \n",
            " 2   venue           76014 non-null  object \n",
            " 3   batting_team    76014 non-null  object \n",
            " 4   bowling_team    76014 non-null  object \n",
            " 5   batsman         76014 non-null  object \n",
            " 6   bowler          76014 non-null  object \n",
            " 7   runs            76014 non-null  int64  \n",
            " 8   wickets         76014 non-null  int64  \n",
            " 9   overs           76014 non-null  float64\n",
            " 10  runs_last_5     76014 non-null  int64  \n",
            " 11  wickets_last_5  76014 non-null  int64  \n",
            " 12  striker         76014 non-null  int64  \n",
            " 13  non-striker     76014 non-null  int64  \n",
            " 14  total           76014 non-null  int64  \n",
            "dtypes: float64(1), int64(8), object(6)\n",
            "memory usage: 8.7+ MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YWmwXKCK4huV",
        "outputId": "fcfc81af-4453-4af4-fd1d-41fd983ec002",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Number of Unique Values in each column\n",
        "data.nunique()"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "mid               617\n",
              "date              442\n",
              "venue              35\n",
              "batting_team       14\n",
              "bowling_team       14\n",
              "batsman           411\n",
              "bowler            329\n",
              "runs              252\n",
              "wickets            11\n",
              "overs             140\n",
              "runs_last_5       102\n",
              "wickets_last_5      8\n",
              "striker           155\n",
              "non-striker        88\n",
              "total             138\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9WvhLdlTaEdt",
        "outputId": "f813d21f-7a66-4ec1-dd23-c0c2b6f540e5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Datatypes of all Columns\n",
        "data.dtypes"
      ],
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "mid                 int64\n",
              "date               object\n",
              "venue              object\n",
              "batting_team       object\n",
              "bowling_team       object\n",
              "batsman            object\n",
              "bowler             object\n",
              "runs                int64\n",
              "wickets             int64\n",
              "overs             float64\n",
              "runs_last_5         int64\n",
              "wickets_last_5      int64\n",
              "striker             int64\n",
              "non-striker         int64\n",
              "total               int64\n",
              "dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dxFkLRRI8RTi"
      },
      "source": [
        "# Data Cleaning"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "s0bwc9vT-7Th"
      },
      "source": [
        "#### Removing Irrelevant Data colunms"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hb-QjD1a6tRs",
        "outputId": "bd7e0636-b2b7-4cce-8066-a06d7411261c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Names of all columns\n",
        "data.columns"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['mid', 'date', 'venue', 'batting_team', 'bowling_team', 'batsman',\n",
              "       'bowler', 'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5',\n",
              "       'striker', 'non-striker', 'total'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kcBf3QuOgzZY"
      },
      "source": [
        "Here, we can see that columns _['mid', 'date', 'venue', 'batsman', 'bowler', 'striker', 'non-striker']_ won't provide any relevant information for our model to train"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0o4-CkhP8W2f",
        "outputId": "34049afd-b8d2-4ef5-9405-94ef2c8a5f23",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "source": [
        "irrelevant = ['mid', 'date', 'venue','batsman', 'bowler', 'striker', 'non-striker']\n",
        "print(f'Before Removing Irrelevant Columns : {data.shape}')\n",
        "data = data.drop(irrelevant, axis=1) # Drop Irrelevant Columns\n",
        "print(f'After Removing Irrelevant Columns : {data.shape}')\n",
        "data.head()"
      ],
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Before Removing Irrelevant Columns : (76014, 15)\n",
            "After Removing Irrelevant Columns : (76014, 8)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>batting_team</th>\n",
              "      <th>bowling_team</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.3</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.4</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            batting_team                 bowling_team  ...  wickets_last_5  total\n",
              "0  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "1  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "2  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "3  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "4  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "\n",
              "[5 rows x 8 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1h2boQJQ-iQp"
      },
      "source": [
        "#### Keeping only Consistent Teams \n",
        "(teams that never change even in current season)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J1LFaSI_8rF7"
      },
      "source": [
        "# Define Consistent Teams\n",
        "const_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',\n",
        "              'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',\n",
        "              'Delhi Daredevils', 'Sunrisers Hyderabad']"
      ],
      "execution_count": 49,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G6r3wXug-z5r",
        "outputId": "a2ce10ac-0e42-427b-96e1-815bcc46dce8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 306
        }
      },
      "source": [
        "print(f'Before Removing Inconsistent Teams : {data.shape}')\n",
        "data = data[(data['batting_team'].isin(const_teams)) & (data['bowling_team'].isin(const_teams))]\n",
        "print(f'After Removing Irrelevant Columns : {data.shape}')\n",
        "print(f\"Consistent Teams : \\n{data['batting_team'].unique()}\")\n",
        "data.head()"
      ],
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Before Removing Inconsistent Teams : (76014, 8)\n",
            "After Removing Irrelevant Columns : (53811, 8)\n",
            "Consistent Teams : \n",
            "['Kolkata Knight Riders' 'Chennai Super Kings' 'Rajasthan Royals'\n",
            " 'Mumbai Indians' 'Kings XI Punjab' 'Royal Challengers Bangalore'\n",
            " 'Delhi Daredevils' 'Sunrisers Hyderabad']\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>batting_team</th>\n",
              "      <th>bowling_team</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.3</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0.4</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            batting_team                 bowling_team  ...  wickets_last_5  total\n",
              "0  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "1  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "2  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "3  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "4  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "\n",
              "[5 rows x 8 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DeyQw7ipA1-r"
      },
      "source": [
        "#### Remove First 5 Overs of every match"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A6zO88dj_5Q7",
        "outputId": "57222977-d7d5-4535-9c02-e37e74647e0a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "source": [
        "print(f'Before Removing Overs : {data.shape}')\n",
        "data = data[data['overs'] >= 5.0]\n",
        "print(f'After Removing Overs : {data.shape}')\n",
        "data.head()"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Before Removing Overs : (53811, 8)\n",
            "After Removing Overs : (40108, 8)\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>batting_team</th>\n",
              "      <th>bowling_team</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>61</td>\n",
              "      <td>0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>59</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.2</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>34</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.3</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.4</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>36</th>\n",
              "      <td>Kolkata Knight Riders</td>\n",
              "      <td>Royal Challengers Bangalore</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.5</td>\n",
              "      <td>58</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "             batting_team                 bowling_team  ...  wickets_last_5  total\n",
              "32  Kolkata Knight Riders  Royal Challengers Bangalore  ...               0    222\n",
              "33  Kolkata Knight Riders  Royal Challengers Bangalore  ...               1    222\n",
              "34  Kolkata Knight Riders  Royal Challengers Bangalore  ...               1    222\n",
              "35  Kolkata Knight Riders  Royal Challengers Bangalore  ...               1    222\n",
              "36  Kolkata Knight Riders  Royal Challengers Bangalore  ...               1    222\n",
              "\n",
              "[5 rows x 8 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DaD8s97SnlnO"
      },
      "source": [
        "Plotting a Correlation Matrix of current data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UDV9JNrZkvZ1",
        "outputId": "f8172e64-0d06-4b92-f9e5-9b6b63481b49",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 348
        }
      },
      "source": [
        "from seaborn import heatmap\n",
        "heatmap(data=data.corr(), annot=True)"
      ],
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fc89bb99ef0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9AjtN9yMEmT0"
      },
      "source": [
        "# Data Preprocessing and Encoding"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cGhNAvUxiy2p"
      },
      "source": [
        "#### Performing Label Encoding"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pw2DBRSAB478",
        "outputId": "82325061-4ed7-4c7e-868f-b66dcebed0d7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
        "le = LabelEncoder()\n",
        "for col in ['batting_team', 'bowling_team']:\n",
        "  data[col] = le.fit_transform(data[col])\n",
        "data.head()"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>batting_team</th>\n",
              "      <th>bowling_team</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>61</td>\n",
              "      <td>0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>59</td>\n",
              "      <td>0</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.2</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>34</th>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.3</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.4</td>\n",
              "      <td>59</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>36</th>\n",
              "      <td>3</td>\n",
              "      <td>6</td>\n",
              "      <td>61</td>\n",
              "      <td>1</td>\n",
              "      <td>5.5</td>\n",
              "      <td>58</td>\n",
              "      <td>1</td>\n",
              "      <td>222</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    batting_team  bowling_team  runs  ...  runs_last_5  wickets_last_5  total\n",
              "32             3             6    61  ...           59               0    222\n",
              "33             3             6    61  ...           59               1    222\n",
              "34             3             6    61  ...           59               1    222\n",
              "35             3             6    61  ...           59               1    222\n",
              "36             3             6    61  ...           58               1    222\n",
              "\n",
              "[5 rows x 8 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fOGcIT_kjBbp"
      },
      "source": [
        "#### Performing One Hot Encoding and Column Transformation"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gTBquJ09Fqpr"
      },
      "source": [
        "from sklearn.compose import ColumnTransformer\n",
        "columnTransformer = ColumnTransformer([('encoder', \n",
        "                                        OneHotEncoder(), \n",
        "                                        [0, 1])], \n",
        "                                      remainder='passthrough')"
      ],
      "execution_count": 54,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WHBT1Y68GcJn"
      },
      "source": [
        "data = np.array(columnTransformer.fit_transform(data))"
      ],
      "execution_count": 55,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dtvG6fLUjlPV"
      },
      "source": [
        "Save the Numpy Array in a new DataFrame with transformed columns"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qQavBDKHGia1"
      },
      "source": [
        "cols = ['batting_team_Chennai Super Kings', 'batting_team_Delhi Daredevils', 'batting_team_Kings XI Punjab',\n",
        "              'batting_team_Kolkata Knight Riders', 'batting_team_Mumbai Indians', 'batting_team_Rajasthan Royals',\n",
        "              'batting_team_Royal Challengers Bangalore', 'batting_team_Sunrisers Hyderabad',\n",
        "              'bowling_team_Chennai Super Kings', 'bowling_team_Delhi Daredevils', 'bowling_team_Kings XI Punjab',\n",
        "              'bowling_team_Kolkata Knight Riders', 'bowling_team_Mumbai Indians', 'bowling_team_Rajasthan Royals',\n",
        "              'bowling_team_Royal Challengers Bangalore', 'bowling_team_Sunrisers Hyderabad', 'runs', 'wickets', 'overs',\n",
        "       'runs_last_5', 'wickets_last_5', 'total']\n",
        "df = pd.DataFrame(data, columns=cols)"
      ],
      "execution_count": 56,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M77XEk1VGjxo",
        "outputId": "8cb827ec-ff94-40d7-bab2-43c27e61a1f5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 258
        }
      },
      "source": [
        "# Visualize Encoded Data\n",
        "df.head()"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>batting_team_Chennai Super Kings</th>\n",
              "      <th>batting_team_Delhi Daredevils</th>\n",
              "      <th>batting_team_Kings XI Punjab</th>\n",
              "      <th>batting_team_Kolkata Knight Riders</th>\n",
              "      <th>batting_team_Mumbai Indians</th>\n",
              "      <th>batting_team_Rajasthan Royals</th>\n",
              "      <th>batting_team_Royal Challengers Bangalore</th>\n",
              "      <th>batting_team_Sunrisers Hyderabad</th>\n",
              "      <th>bowling_team_Chennai Super Kings</th>\n",
              "      <th>bowling_team_Delhi Daredevils</th>\n",
              "      <th>bowling_team_Kings XI Punjab</th>\n",
              "      <th>bowling_team_Kolkata Knight Riders</th>\n",
              "      <th>bowling_team_Mumbai Indians</th>\n",
              "      <th>bowling_team_Rajasthan Royals</th>\n",
              "      <th>bowling_team_Royal Challengers Bangalore</th>\n",
              "      <th>bowling_team_Sunrisers Hyderabad</th>\n",
              "      <th>runs</th>\n",
              "      <th>wickets</th>\n",
              "      <th>overs</th>\n",
              "      <th>runs_last_5</th>\n",
              "      <th>wickets_last_5</th>\n",
              "      <th>total</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>59.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>222.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>222.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5.3</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>222.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5.4</td>\n",
              "      <td>59.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>222.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>0.0</td>\n",
              "      <td>61.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>5.5</td>\n",
              "      <td>58.0</td>\n",
              "      <td>1.0</td>\n",
              "      <td>222.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   batting_team_Chennai Super Kings  ...  total\n",
              "0                               0.0  ...  222.0\n",
              "1                               0.0  ...  222.0\n",
              "2                               0.0  ...  222.0\n",
              "3                               0.0  ...  222.0\n",
              "4                               0.0  ...  222.0\n",
              "\n",
              "[5 rows x 22 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t6kAENbRH7zF"
      },
      "source": [
        "# Model Building"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4_zfjKeoH-5C"
      },
      "source": [
        "## Prepare Train and Test Splits"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tLK1yUvnGuDw"
      },
      "source": [
        "features = df.drop(['total'], axis=1)\n",
        "labels = df['total']"
      ],
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yR7cmz0tIhZW",
        "outputId": "b6eec663-81e1-4dae-c12d-a600d6c24a0d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Perform 80 : 20 Train-Test split\n",
        "from sklearn.model_selection import train_test_split\n",
        "train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.20, shuffle=True)\n",
        "print(f\"Training Set : {train_features.shape}\\nTesting Set : {test_features.shape}\")"
      ],
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Training Set : (32086, 21)\n",
            "Testing Set : (8022, 21)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J5ZhNp2EJ37b"
      },
      "source": [
        "## Model Algorithms\n",
        "Training and Testing on different Machine Learning Algorithms for the best algorithm to choose from"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xPgXWd3rKTnA"
      },
      "source": [
        "# Keeping track of model perfomances\n",
        "models = dict()"
      ],
      "execution_count": 60,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T7HfUM1mKK2u"
      },
      "source": [
        "#### 1. Decision Tree Regressor"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_X6OA45yJx0P",
        "outputId": "02fb3631-7054-4926-a98c-bc112d9f2127",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.tree import DecisionTreeRegressor\n",
        "tree = DecisionTreeRegressor()\n",
        "# Train Model\n",
        "tree.fit(train_features, train_labels)"
      ],
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DecisionTreeRegressor(ccp_alpha=0.0, criterion='mse', max_depth=None,\n",
              "                      max_features=None, max_leaf_nodes=None,\n",
              "                      min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                      min_samples_leaf=1, min_samples_split=2,\n",
              "                      min_weight_fraction_leaf=0.0, presort='deprecated',\n",
              "                      random_state=None, splitter='best')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S_kaCtenKiME",
        "outputId": "20fb5f6e-b964-4f6f-d72b-500979e51366",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Evaluate Model\n",
        "train_score_tree = str(tree.score(train_features, train_labels) * 100)\n",
        "test_score_tree = str(tree.score(test_features, test_labels) * 100)\n",
        "print(f'Train Score : {train_score_tree[:5]}%\\nTest Score : {test_score_tree[:5]}%')\n",
        "models[\"tree\"] = test_score_tree"
      ],
      "execution_count": 62,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 99.98%\n",
            "Test Score : 86.13%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JPNUcmG0TwoK",
        "outputId": "5dbb3b2d-f7bb-467e-a479-85ff5e18bf45",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse\n",
        "print(\"---- Decision Tree Regressor - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, tree.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, tree.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, tree.predict(test_features)))))"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Decision Tree Regressor - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 3.9665918723510347\n",
            "Mean Squared Error (MSE): 122.64298180004987\n",
            "Root Mean Squared Error (RMSE): 11.0744291861951\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0F9fVUPuMwX0"
      },
      "source": [
        "#### Linear Regression"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RvNDa8MGdYYs",
        "outputId": "2e6b298e-9251-4ff5-ac12-61062b503afe",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "linreg = LinearRegression()\n",
        "# Train Model\n",
        "linreg.fit(train_features, train_labels)"
      ],
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 64
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kHOQcP-PQGYq",
        "outputId": "623d00bb-72e4-4bc6-8fd8-352300932ff0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Evaluate Model\n",
        "train_score_linreg = str(linreg.score(train_features, train_labels) * 100)\n",
        "test_score_linreg = str(linreg.score(test_features, test_labels) * 100)\n",
        "print(f'Train Score : {train_score_linreg[:5]}%\\nTest Score : {test_score_linreg[:5]}%')\n",
        "models[\"linreg\"] = test_score_linreg"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 65.91%\n",
            "Test Score : 65.91%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nVSzI12HRnnF",
        "outputId": "317d6160-f826-46f5-dff2-faf0740edc4e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"---- Linear Regression - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, linreg.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, linreg.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, linreg.predict(test_features)))))"
      ],
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Linear Regression - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 13.095521348645773\n",
            "Mean Squared Error (MSE): 301.4403800998092\n",
            "Root Mean Squared Error (RMSE): 17.36203847766181\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PPjZxiqnT3NC"
      },
      "source": [
        "#### Random Forest Regression"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ub06meKxTlZh",
        "outputId": "1517fdfc-b414-47d8-ee6c-a8131df1b584",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.ensemble import RandomForestRegressor\n",
        "forest = RandomForestRegressor()\n",
        "# Train Model\n",
        "forest.fit(train_features, train_labels)"
      ],
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mse',\n",
              "                      max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
              "                      max_samples=None, min_impurity_decrease=0.0,\n",
              "                      min_impurity_split=None, min_samples_leaf=1,\n",
              "                      min_samples_split=2, min_weight_fraction_leaf=0.0,\n",
              "                      n_estimators=100, n_jobs=None, oob_score=False,\n",
              "                      random_state=None, verbose=0, warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o3o7ax7BUOke",
        "outputId": "73858c9e-f846-4e93-f694-886cd3fbaae5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Evaluate Model\n",
        "train_score_forest = str(forest.score(train_features, train_labels)*100)\n",
        "test_score_forest = str(forest.score(test_features, test_labels)*100)\n",
        "print(f'Train Score : {train_score_forest[:5]}%\\nTest Score : {test_score_forest[:5]}%')\n",
        "models[\"forest\"] = test_score_forest"
      ],
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 99.07%\n",
            "Test Score : 93.08%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r82lD-fkebkn",
        "outputId": "e49419bd-39d9-4029-95b5-63f88596bc9c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"---- Random Forest Regression - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, forest.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, forest.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, forest.predict(test_features)))))"
      ],
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Random Forest Regression - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 4.608180013890372\n",
            "Mean Squared Error (MSE): 61.16125239745949\n",
            "Root Mean Squared Error (RMSE): 7.820565989585376\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KQ4gOn5nd_31"
      },
      "source": [
        "#### Lasso Regression"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FM5UDCyAeHcS",
        "outputId": "48f3c47d-63e5-4df1-b1de-7d83f656e1a5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.linear_model import LassoCV\n",
        "lasso = LassoCV()\n",
        "# Train Model\n",
        "lasso.fit(train_features, train_labels)"
      ],
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LassoCV(alphas=None, copy_X=True, cv=None, eps=0.001, fit_intercept=True,\n",
              "        max_iter=1000, n_alphas=100, n_jobs=None, normalize=False,\n",
              "        positive=False, precompute='auto', random_state=None,\n",
              "        selection='cyclic', tol=0.0001, verbose=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 70
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RMBloU5SemTJ",
        "outputId": "6784ebda-6770-443b-8fdb-be067ab108db",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Evaluate Model\n",
        "train_score_lasso = str(lasso.score(train_features, train_labels)*100)\n",
        "test_score_lasso = str(lasso.score(test_features, test_labels)*100)\n",
        "print(f'Train Score : {train_score_lasso[:5]}%\\nTest Score : {test_score_lasso[:5]}%')\n",
        "models[\"lasso\"] = test_score_lasso"
      ],
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 64.89%\n",
            "Test Score : 64.96%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PgQY888hej2W",
        "outputId": "9a85de83-9e86-4412-8538-d4f1239a2a19",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"---- Lasso Regression - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, lasso.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, lasso.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, lasso.predict(test_features)))))"
      ],
      "execution_count": 72,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Lasso Regression - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 13.11601746800165\n",
            "Mean Squared Error (MSE): 309.8797484347863\n",
            "Root Mean Squared Error (RMSE): 17.603401615448824\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "64qH8gtlev5U"
      },
      "source": [
        "#### Support Vector Machine"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YzJJ9DUUezZj",
        "outputId": "776bee60-752e-4713-ef65-e241da87c4a8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.svm import SVR\n",
        "svm = SVR()\n",
        "# Train Model\n",
        "svm.fit(train_features, train_labels)"
      ],
      "execution_count": 73,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='scale',\n",
              "    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sqLSvMIce_Pt",
        "outputId": "41b79eef-6080-4a8f-a1f8-236e3a3afd50",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "train_score_svm = str(svm.score(train_features, train_labels)*100)\n",
        "test_score_svm = str(svm.score(test_features, test_labels)*100)\n",
        "print(f'Train Score : {train_score_svm[:5]}%\\nTest Score : {test_score_svm[:5]}%')\n",
        "models[\"svm\"] = test_score_svm "
      ],
      "execution_count": 74,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 57.48%\n",
            "Test Score : 57.45%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5fSWYF30jxLr",
        "outputId": "7387988f-2dd7-4e95-a6c2-4e24ecefd45f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"---- Support Vector Regression - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, svm.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, svm.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, svm.predict(test_features)))))"
      ],
      "execution_count": 75,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Support Vector Regression - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 14.689273833142883\n",
            "Mean Squared Error (MSE): 376.2689686154565\n",
            "Root Mean Squared Error (RMSE): 19.39765368840924\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rRroeuZElfea"
      },
      "source": [
        "#### Neural Networks"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YMQL5K7EkAuB",
        "outputId": "4be4a1a0-46f9-475f-e48c-9c27c68325fe",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from sklearn.neural_network import MLPRegressor\n",
        "neural_net = MLPRegressor(activation='logistic', max_iter=500)\n",
        "# Train Model\n",
        "neural_net.fit(train_features, train_labels)"
      ],
      "execution_count": 76,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/sklearn/neural_network/_multilayer_perceptron.py:571: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (500) reached and the optimization hasn't converged yet.\n",
            "  % self.max_iter, ConvergenceWarning)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "MLPRegressor(activation='logistic', alpha=0.0001, batch_size='auto', beta_1=0.9,\n",
              "             beta_2=0.999, early_stopping=False, epsilon=1e-08,\n",
              "             hidden_layer_sizes=(100,), learning_rate='constant',\n",
              "             learning_rate_init=0.001, max_fun=15000, max_iter=500,\n",
              "             momentum=0.9, n_iter_no_change=10, nesterovs_momentum=True,\n",
              "             power_t=0.5, random_state=None, shuffle=True, solver='adam',\n",
              "             tol=0.0001, validation_fraction=0.1, verbose=False,\n",
              "             warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XlSAZ_4skUDj",
        "outputId": "ca202fbc-13e3-4ea6-8113-53d607c10279",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "train_score_neural_net = str(neural_net.score(train_features, train_labels)*100)\n",
        "test_score_neural_net = str(neural_net.score(test_features, test_labels)*100)\n",
        "print(f'Train Score : {train_score_neural_net[:5]}%\\nTest Score : {test_score_neural_net[:5]}%')\n",
        "models[\"neural_net\"] = test_score_neural_net "
      ],
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Train Score : 86.27%\n",
            "Test Score : 84.68%\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1xhaNnp-kRkG",
        "outputId": "57becd58-0456-43b4-c3f4-c881f95d11ab",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"---- Neural Networks Regression - Model Evaluation ----\")\n",
        "print(\"Mean Absolute Error (MAE): {}\".format(mae(test_labels, neural_net.predict(test_features))))\n",
        "print(\"Mean Squared Error (MSE): {}\".format(mse(test_labels, neural_net.predict(test_features))))\n",
        "print(\"Root Mean Squared Error (RMSE): {}\".format(np.sqrt(mse(test_labels, neural_net.predict(test_features)))))"
      ],
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "---- Neural Networks Regression - Model Evaluation ----\n",
            "Mean Absolute Error (MAE): 8.252417080313622\n",
            "Mean Squared Error (MSE): 135.47139255624822\n",
            "Root Mean Squared Error (RMSE): 11.639217867032485\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_iUiJYZzpF0e"
      },
      "source": [
        "## Best Model Selection"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dAJYQS-gUoAT",
        "outputId": "41b4d5d8-9b2c-40f2-e628-dab0c6e87506",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 337
        }
      },
      "source": [
        "from seaborn import barplot\n",
        "model_names = list(models.keys())\n",
        "accuracy = list(map(float, models.values()))\n",
        "barplot(model_names, accuracy)"
      ],
      "execution_count": 80,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
            "  FutureWarning\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fc89ba2f6a0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 80
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1aZkPTi3rlzP"
      },
      "source": [
        "From above, we can see that **Random Forest** performed the best, closely followed by **Decision Tree** and **Neural Networks**. So we will be choosing Random Forest for the final model"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZXZ8NE5hgbd2"
      },
      "source": [
        "# Predictions"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QrWfMFKCU7Zu"
      },
      "source": [
        "def predict_score(batting_team, bowling_team, runs, wickets, overs, runs_last_5, wickets_last_5, model=forest):\n",
        "  prediction_array = []\n",
        "  # Batting Team\n",
        "  if batting_team == 'Chennai Super Kings':\n",
        "    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]\n",
        "  elif batting_team == 'Delhi Daredevils':\n",
        "    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]\n",
        "  elif batting_team == 'Kings XI Punjab':\n",
        "    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]\n",
        "  elif batting_team == 'Kolkata Knight Riders':\n",
        "    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]\n",
        "  elif batting_team == 'Mumbai Indians':\n",
        "    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]\n",
        "  elif batting_team == 'Rajasthan Royals':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]\n",
        "  elif batting_team == 'Royal Challengers Bangalore':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]\n",
        "  elif batting_team == 'Sunrisers Hyderabad':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]\n",
        "  # Bowling Team\n",
        "  if bowling_team == 'Chennai Super Kings':\n",
        "    prediction_array = prediction_array + [1,0,0,0,0,0,0,0]\n",
        "  elif bowling_team == 'Delhi Daredevils':\n",
        "    prediction_array = prediction_array + [0,1,0,0,0,0,0,0]\n",
        "  elif bowling_team == 'Kings XI Punjab':\n",
        "    prediction_array = prediction_array + [0,0,1,0,0,0,0,0]\n",
        "  elif bowling_team == 'Kolkata Knight Riders':\n",
        "    prediction_array = prediction_array + [0,0,0,1,0,0,0,0]\n",
        "  elif bowling_team == 'Mumbai Indians':\n",
        "    prediction_array = prediction_array + [0,0,0,0,1,0,0,0]\n",
        "  elif bowling_team == 'Rajasthan Royals':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,1,0,0]\n",
        "  elif bowling_team == 'Royal Challengers Bangalore':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,0,1,0]\n",
        "  elif bowling_team == 'Sunrisers Hyderabad':\n",
        "    prediction_array = prediction_array + [0,0,0,0,0,0,0,1]\n",
        "  prediction_array = prediction_array + [runs, wickets, overs, runs_last_5, wickets_last_5]\n",
        "  prediction_array = np.array([prediction_array])\n",
        "  pred = model.predict(prediction_array)\n",
        "  return int(round(pred[0]))"
      ],
      "execution_count": 81,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SY2cbaHfgdrV"
      },
      "source": [
        "### Test 1\n",
        "- Batting Team : **Delhi Daredevils**\n",
        "- Bowling Team : **Chennai Super Kings**\n",
        "- Final Score : **147/9**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s3xhyRdYW4f6",
        "outputId": "2a518819-7dd9-41c0-9e75-7bf1a0d13944",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "batting_team='Delhi Daredevils'\n",
        "bowling_team='Chennai Super Kings'\n",
        "score = predict_score(batting_team, bowling_team, overs=10.2, runs=68, wickets=3, runs_last_5=29, wickets_last_5=1)\n",
        "print(f'Predicted Score : {score} || Actual Score : 147')"
      ],
      "execution_count": 82,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 147 || Actual Score : 147\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HsKOgxEZhFVO"
      },
      "source": [
        "### Test 2\n",
        "- Batting Team : **Mumbai Indians**\n",
        "- Bowling Team : **Kings XI Punjab**\n",
        "- Final Score : **176/7**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QWA1KTdpX9Za",
        "outputId": "7818155a-80be-4756-bfd6-1c5a459f06d8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "batting_team='Mumbai Indians'\n",
        "bowling_team='Kings XI Punjab'\n",
        "score = predict_score(batting_team, bowling_team, overs=12.3, runs=113, wickets=2, runs_last_5=55, wickets_last_5=0)\n",
        "print(f'Predicted Score : {score} || Actual Score : 176')"
      ],
      "execution_count": 83,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 189 || Actual Score : 176\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RzKmW6BchwKW"
      },
      "source": [
        "### Live* Test 1 (2020 season)\n",
        "- Batting Team : **Kings XI Punjab**\n",
        "- Bowling Team : **Rajasthan Royals**\n",
        "- Final Score : **185/4**\n",
        "<br/>\n",
        "These Test Was done before the match and final score were added later."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "80NScDvNYZ2K",
        "outputId": "5a974fe8-4028-47ce-bc21-e8ce322b6e48",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Live Test\n",
        "batting_team=\"Kings XI Punjab\"\n",
        "bowling_team=\"Rajasthan Royals\"\n",
        "score = predict_score(batting_team, bowling_team, overs=14.0, runs=118, wickets=1, runs_last_5=45, wickets_last_5=0)\n",
        "print(f'Predicted Score : {score} || Actual Score : 185')"
      ],
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 178 || Actual Score : 185\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ta72D9zFiCd1"
      },
      "source": [
        "### Live Test 2 (2020 Season)\n",
        "- Batting Team : **Kolkata Knight Riders**\n",
        "- Bowling Team : **Chennai Super Kings**\n",
        "- Final Score : **172/5**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NQ6dHS_YaQJ9",
        "outputId": "8efb796b-b413-4cbd-908d-386db710c59f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Live Test\n",
        "batting_team=\"Kolkata Knight Riders\"\n",
        "bowling_team=\"Chennai Super Kings\"\n",
        "score = predict_score(batting_team, bowling_team, overs=18.0, runs=150, wickets=4, runs_last_5=57, wickets_last_5=1)\n",
        "print(f'Predicted Score : {score} || Actual Score : 172')"
      ],
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 175 || Actual Score : 172\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WKwPjoaDzgKf"
      },
      "source": [
        "### Live Test 3 (2020 Season)\n",
        "- Batting Team : **Delhi Daredevils**\n",
        "- Bowling Team : **Mumbai Indians**\n",
        "- Final Score : **110/7**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pdghw3mhzv0b",
        "outputId": "16d7798b-4e1b-4c50-8690-a7361c1e28e8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "batting_team='Delhi Daredevils'\n",
        "bowling_team='Mumbai Indians'\n",
        "score = predict_score(batting_team, bowling_team, overs=18.0, runs=96, wickets=8, runs_last_5=18, wickets_last_5=4)\n",
        "print(f'Predicted Score : {score} || Actual Score : 110')"
      ],
      "execution_count": 87,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 107 || Actual Score : 110\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dkIDqCkg0DWM"
      },
      "source": [
        "### Live Test 4 (2020 Season)\n",
        "- Batting Team : **Kings XI Punjab**\n",
        "- Bowling Team : **Chennai Super Kings**\n",
        "- Final Score : **153/9**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DAcEBGuw0ck8",
        "outputId": "abab316a-3aad-427d-9225-07861bd969f9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "batting_team='Kings XI Punjab'\n",
        "bowling_team='Chennai Super Kings'\n",
        "score = predict_score(batting_team, bowling_team, overs=18.0, runs=129, wickets=6, runs_last_5=34, wickets_last_5=2)\n",
        "print(f'Predicted Score : {score} || Actual Score : 153')"
      ],
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Predicted Score : 147 || Actual Score : 153\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UReOWOeQiSD-"
      },
      "source": [
        "# Export Model"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z8q6lNENfWlY",
        "outputId": "b9899d46-86f2-44b7-88ca-89fcc720621c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "from joblib import dump\n",
        "\n",
        "dump(forest, \"forest_model.pkl\")\n",
        "dump(tree, \"tree_model.pkl\")\n",
        "dump(neural_net, \"neural_nets_model.pkl\")"
      ],
      "execution_count": 92,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['neural_nets_model.pkl']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AzjKpBWh03z_"
      },
      "source": [
        ""
      ],
      "execution_count": nullcontext,
      "outputs": []
    }
  ]
}