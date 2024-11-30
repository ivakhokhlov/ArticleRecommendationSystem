<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Рекомендации статей по запросу</h1>
  
      <!-- Поле для ввода текста запроса -->
      <textarea
        v-model="query"
        placeholder="Введите текстовый запрос"
        rows="5"
        class="w-full p-2 border border-gray-300 rounded mb-4"
      ></textarea>
  
      <!-- Кнопка для отправки запроса -->
      <button
        @click="fetchRecommendations"
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Найти статьи
      </button>
  
      <!-- Отображение результатов -->
      <div v-if="recommendations.length" class="mt-4">
        <h2 class="text-xl font-semibold mb-2">Рекомендованные статьи:</h2>
        <ul>
          <li v-for="article in recommendations" :key="article.id" class="mb-2">
            <h3 class="text-lg font-bold">{{ article.title }}</h3>
            <p>{{ article.summary }}</p>
          </li>
        </ul>
      </div>
  
      <!-- Сообщение об ошибке -->
      <div v-if="error" class="mt-4 text-red-500">
        Ошибка: {{ error }}
      </div>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
  
    export default {
      name: 'HomeView',
      data() {
        return {
          query: '',
          recommendations: [],
          error: null,
        };
      },
      methods: {
        async fetchRecommendations() {
          await axios
            .post("http://localhost:8000/recommend", {
              query: this.query,
            })
            .then((response) => {
              this.recommendations = response.data.recommendations; // Сохраняем рекомендации
              this.error = null; // Сбрасываем ошибку
            })
            .catch((error) => {
              this.error = "Не удалось получить рекомендации";
              console.error("error", error);
            });
        },
      },
    };
  </script>
  
  <style scoped>
    .container {
      max-width: 500px;
    }
  </style>
  