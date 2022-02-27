{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "MarketAndMachineLearning3.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMcWYyKAdxtEB8qUZjDrHw7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/msunglim/machineLearningAlone/blob/main/MarketAndMachineLearning3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "trKhj3YfiLV6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 558
        },
        "id": "VInMePPDVZcC",
        "outputId": "3c4bfb81-1de4-4969-dfbd-408324a3ed68"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.]\n"
          ]
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
            "needs_background": "light"
          }
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
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# domi\n",
        "bream_length = [25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.7,30.9,31.0,31.0,31.5,32.0,32.0,33.0,33.5,33.5,34.0,34.0]\n",
        "bream_weight= [430.3,450.0,460.0,490.0,450.0,500.0,475.0,500.0,500.0,540.0,600.0,600.0,610.0,615.0,610.0,650.0,675.0,685.0,620.0,680.0]\n",
        "# print(len(bream_length))= 20\n",
        "\n",
        "# binga\n",
        "smelt_length =[9.8,10.5,10.6,11.0,11.2,11.3,11.5,11.8,11.9,12.0,12.2,12.4,13.0,15.0]\n",
        "smelt_weight=[6.7,7.5,7.0,9.7,9.8,8.7,10.0,9.9,9.8,12.2,13.4,12.2,19.7,19.9]\n",
        "# print(len(smelt_length)) = 14\n",
        "\n",
        "# --------------------\n",
        "length = bream_length + smelt_length\n",
        "weight = bream_weight+ smelt_weight\n",
        "fish_data = np.column_stack((length, weight))\n",
        "\n",
        "# fish_target is like an answer sheet \n",
        "# fish_target = [1]*len(bream_length) + [0]*len(smelt_length)\n",
        "fish_target = np.concatenate((np.ones(len(bream_length)), np.zeros(len(smelt_length))))\n",
        "\n",
        "# input_arr = np.array(fish_data)\n",
        "# target_arr = np.array(fish_target)\n",
        "\n",
        "# index = np.arange(len(bream_length)+len(smelt_length))\n",
        "# np.random.shuffle(index)\n",
        "\n",
        "# train_input = input_arr[index[:len(bream_length)]]\n",
        "# train_target = target_arr[index[:len(bream_length)]]\n",
        "\n",
        "# test_input = input_arr[index[len(bream_length):]]\n",
        "# test_target= target_arr[index[len(bream_length):]]\n",
        "\n",
        "train_input, test_input, train_target, test_target = train_test_split(\n",
        "    fish_data, fish_target, stratify= fish_target, random_state=len(fish_data))\n",
        "\n",
        "# well mixed dataset\n",
        "kn = KNeighborsClassifier()\n",
        "kn = kn.fit(train_input, train_target)\n",
        "\n",
        "kn.score(test_input, test_target)\n",
        "#this test returns array[0] which means it is smelt.\n",
        "print(kn.predict([[25,150]]))\n",
        "\n",
        "#returns distance from point to its neighbors and indexes of neighbors based on Kn_neighbors \n",
        "distances, indexes = kn.kneighbors([[25,150]])\n",
        "# print(distances) index is generated based on the graph.\n",
        "# print(indexes)\n",
        "\n",
        "plt.scatter(train_input[:,0], train_input[:, 1])\n",
        "# mark triangle on input point\n",
        "plt.scatter(25,150, marker= '^')\n",
        "\n",
        "# mark diamond on points close to input point \n",
        "plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')\n",
        "\n",
        "# plt.xlim(0,700)\n",
        "plt.xlabel('length')\n",
        "plt.ylabel('weight')\n",
        "plt.show()\n",
        "\n",
        "#-------------------------------------\n",
        "#Main Idea\n",
        "#scaled graph\n",
        "\n",
        "mean = np.mean(train_input, axis=0)\n",
        "std = np.std(train_input, axis=0)\n",
        "\n",
        "train_scaled = (train_input - mean)/std\n",
        "\n",
        "kn = kn.fit(train_scaled, train_target)\n",
        "\n",
        "test_scaled = (test_input - mean)/std\n",
        "kn.score(test_scaled, test_target)\n",
        "\n",
        "new = ([25,150]- mean)/std\n",
        "distances, indexes = kn.kneighbors([new])\n",
        "\n",
        "plt.scatter(train_scaled[:,0], train_scaled[:, 1])\n",
        "# mark triangle on input point\n",
        "plt.scatter(new[0], new[1], marker = '^')\n",
        "# mark diamond on points close to input point \n",
        "plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')\n",
        "\n",
        "plt.xlabel('length')\n",
        "plt.ylabel('weight')\n",
        "plt.show()\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}