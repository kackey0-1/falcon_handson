<template>
  <v-app>
    <h1>Home page</h1>
    <NuxtLink to="/">
      About (internal link that belongs to the Nuxt App)
    </NuxtLink>
    <a href="https://nuxtjs.org">External Link to another page</a>
  </v-app>
</template>
<script lang="ts">
import {
  Component,
  Vue
} from "nuxt-property-decorator"
import { State } from "vuex-class"
import type { Person } from "~/types";
import Card from "~/components/Card.vue"

@Component({
  components: {
    Card
  }
})
export default class extends Vue {
  @State people!: Person[]
}
</script>

<style scoped>
.header {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

.cards {
  display: flex;
  flex-wrap: wrap;
}
</style>
