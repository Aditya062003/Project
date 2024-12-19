<template>
  <div class="bg-gray-900 text-white">
    <div class="relative overflow-x-hidden py-6">
      <div
        class="absolute z-[0] inset-0 bg-cover bg-center opacity-30"
        :style="`background-image: linear-gradient(to right, rgba(3, 37, 65, 1), rgba(3, 37, 65, 0.6)), url('${movie.Poster}');`"
      ></div>

      <div class="flex flex-col z-20 md:flex-row mx-auto gap-4 p-4">
        <div
          class="w-full z-20 md:w-1/3 flex-shrink-0 flex flex-col items-center"
        >
          <img
            :src="movie.Poster"
            :alt="movie.Title"
            class="w-[24rem] shadow-lg"
          />
          <div
            class="bg-[#032541e1] hidden md:flex justify-center items-center p-2 gap-4 md:w-[24rem]"
          >
            <img
              :src="HOTSTAR_URL"
              alt="The Movie Database (TMDB)"
              width="68"
            />
            <div>
              <div class="text-[1.125rem] text-gray-400">Now Streaming</div>
              <div class="text-[1.125rem] font-medium">Watch Now</div>
            </div>
          </div>
        </div>

        <div class="w-full z-20 my-4 md:w-2/3">
          <h1 class="md:text-5xl text-2xl font-medium">
            {{ movie.Title }}
            <span class="text-gray-400">({{ movie.Year }})</span>
          </h1>
          <div class="flex gap-2 align-middle items-center mt-1">
            <div
              class="border md:text-xl text-sm border-gray-400 text-gray-400 w-fit p-1"
            >
              {{ movie.Rated }}
            </div>
            <div class="text-white font-light p-1">{{ movie.Released }}</div>
            <div class="text-white hidden md:block font-light p-1">
              {{ movie.Genre }}
            </div>
            <div class="text-white font-light p-1">{{ formattedRuntime }}</div>
          </div>

          <div class="flex items-center gap-8">
            <div class="flex items-center md:gap-2">
              <UserScore :value="imdbScore" />

              <div class="flex-col">
                <div class="text-gray-300 text-[1rem] font-bold">User</div>
                <div class="text-gray-300 text-[1rem] font-bold">Score</div>
              </div>
            </div>

            <div class="md:flex hidden items-center space-x-4">
              <div class="bg-[#032541] px-2 py-2 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6 text-gray-300"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 12h12M6 6h12M6 18h12"
                  ></path>
                </svg>
              </div>

              <div class="bg-[#032541] hover:fill-white px-2 py-3 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-4 w-6 fill-white text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 21l-1-1c-5-5-8-7.5-8-11A5 5 0 0112 3a5 5 0 018 6c0 3.5-3 6.5-8 11l-1 1z"
                  ></path>
                </svg>
              </div>

              <div class="bg-[#032541] px-2 py-2 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-6 w-6 text-yellow-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 17l-5.5 3.6 2-6.8-5-4.2h6.2l2-6.8 2 6.8h6.2l-5 4.2 2 6.8L12 17z"
                  ></path>
                </svg>
              </div>
            </div>
            <button
              class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded text-sm font-semibold"
            >
              ▶ Play Trailer
            </button>
          </div>

          <div>
            <h3 class="font-bold text-xl my-2">Overview</h3>
            <p class="text-gray-300">{{ movie.Plot }}</p>
          </div>

          <div class="mt-6">
            <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
              <div v-if="movie.Director">
                <strong class="text-white block text-lg">{{
                  movie.Director
                }}</strong>
                <span class="text-gray-400">Director</span>
              </div>

              <div
                v-for="(writer, index) in movie.Writer.split(', ')"
                :key="'writer-' + index"
              >
                <strong class="text-white block text-lg">{{ writer }}</strong>
                <span class="text-gray-400">Writer</span>
              </div>

              <div
                v-for="(actor, index) in movie.Actors.split(', ')"
                :key="'actor-' + index"
              >
                <strong class="text-white block text-lg">{{ actor }}</strong>
                <span class="text-gray-400">Actor</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="dark:bg-[#032541] bg-gray-100 text-gray-900 dark:text-white py-6"
    >
      <div class="md:flex justify-center md:mx-16 sm:mx-3 relative">
        <div class="md:w-3/4 relative z-10">
          <h2 class="text-xl font-bold mb-4">Top Billed Cast</h2>
          <div class="flex gap-2 space-x-4 overflow-x-auto hide-scrollbar">
            <div
              v-for="actor in cast"
              :key="actor.id"
              class="flex-none dark:bg-slate-600 shadow-xl rounded-lg p-1 text-center w-32"
            >
              <img
                :src="`https://image.tmdb.org/t/p/w300_and_h450_bestv2${actor.profile_path}`"
                :alt="actor.name"
                class="rounded-md object-cover h-40 w-60"
              />
              <p
                class="mt-2 text-sm font-semibold text-gray-900 dark:text-white"
              >
                {{ actor.name }}
              </p>
              <p class="text-sm text-gray-600 dark:text-white">
                {{ actor.character }}
              </p>
            </div>
          </div>
        </div>
        <div class="md:w-1/4 z-20 relative">
          <div class="relative text-left md:block grid grid-cols-2 p-4 z-10">
            <div class="font-bold text-gray-900 dark:text-white">Language</div>
            <div class="font-medium text-gray-700 dark:text-gray-300">
              {{ movie.Language }}
            </div>
            <div class="md:mt-4 font-bold text-gray-900 dark:text-white">
              Revenue
            </div>
            <div class="font-medium text-gray-700 dark:text-gray-300">
              {{ movie.BoxOffice }}
            </div>
            <div class="md:mt-4 font-bold text-gray-900 dark:text-white">
              Country
            </div>
            <div class="font-medium text-gray-700 dark:text-gray-300">
              {{ movie.Country }}
            </div>
            <div class="md:mt-4 font-bold text-gray-900 dark:text-white">
              Rotten Tomatoes 🍅
            </div>
            <div
              v-if="movie.Ratings"
              class="font-medium text-gray-700 dark:text-gray-300"
            >
              {{ movie.Ratings[1].Value }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { HOTSTAR_URL, THUMBNAIL_URL } from "@/Constants";
import UserScore from "@/components/UserScore.vue";

export default {
  components: {
    UserScore,
  },
  data() {
    return {
      movie: {
        Title: "",
        Year: "",
        Rated: "",
        Released: "",
        Runtime: "",
        Genre: "",
        Director: "",
        Writer: "",
        Actors: "",
        Plot: "",
        Poster: "",
      },
      cast: [],
      imdbScore: 0,
      HOTSTAR_URL,
      THUMBNAIL_URL,
    };
  },
  computed: {
    formattedRuntime() {
      if (!this.movie.Runtime || typeof this.movie.Runtime !== "string") {
        return "N/A";
      }

      const runtimeMatch = this.movie.Runtime.match(/\d+/);

      if (runtimeMatch && runtimeMatch[0]) {
        const runtimeInMinutes = parseInt(runtimeMatch[0]);
        const hours = Math.floor(runtimeInMinutes / 60);
        const minutes = runtimeInMinutes % 60;

        return `${hours > 0 ? hours + "h " : ""}${minutes}m`;
      }

      return "N/A";
    },
  },
  mounted() {
    this.fetchMovieData();
    this.fetchCastData();
  },
  methods: {
    async fetchMovieData() {
      try {
        const response = await axios.get(
          "https://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
        );
        this.movie = response.data;
        this.imdbScore = Math.round(parseFloat(response.data.imdbRating) * 10);
      } catch (error) {
        console.error("Error fetching movie data:", error);
      }
    },
    async fetchCastData() {
      try {
        const response = await axios.get(
          "https://api.themoviedb.org/3/movie/283995/credits?api_key=875d22372d43d03775be507dff99cc7c&language=en-US"
        );
        this.cast = response.data.cast.slice(0, 15);
      } catch (error) {
        console.error("Error fetching cast data:", error);
      }
    },
  },
};
</script>

<style scoped>
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}

.flex-none {
  flex-shrink: 0;
}
</style>
