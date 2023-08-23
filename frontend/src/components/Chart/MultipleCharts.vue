<template>
  <div>
    <h2 class="text-center">Promo charts</h2>
    <div v-for="(item, index) in dataArr" :key="index" class="d-flex justify-content-center chart">
      <Bar :data="item" :options="options" v-if="dataArr" />
    </div>

    <h2 class="mt-4 text-center">Brands/Retailer charts</h2>
    <div v-for="(brand, i) in brandDataArr" :key="'brand' + i" class="d-flex justify-content-center chart">
      <Bar :data="brand" :options="options" v-if="brandDataArr" />
    </div>
  </div>
</template>

<script lang="ts">
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
import { Bar } from 'vue-chartjs';
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default {
  name: 'App',
  components: {
    Bar,
  },
  data() {
    return {
      options: {
        responsive: true,
      },
      jsonData: null,
      dataArr: [],
      brandDataArr: [],
      externalUrl:process.env.VUE_APP_URL
    };
  },
  methods: {
    async fetchJsonData(){
      try {
        const response = await fetch(this.externalUrl);
        
        this.jsonData=await response.json()
      } catch (error) {
        console.log('Error fetching data:', error);
      }
    },
    convertToJsonForChart(key, type) {
      //mapping the json into data that can be populated by chart
      const chartData = {
        //populating the keys from json into text specified in locale
        labels: Object.keys(this.jsonData[type][key]).map((e) => this.$t(e)),
        datasets: [
          {
            label: this.$t(key),
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            data: Object.values(this.jsonData[type][key]),
          },
        ],
      };

      return chartData;
    },

    convertToDataArray(jsonObj, type) {
      //method to populate array for chart
      let keyArr = Object.keys(jsonObj);
      let arr = [];
      keyArr.forEach((element) => {
        let obj = this.convertToJsonForChart(element, type);
        arr.push(obj);
      });
      return arr;
    },
  },
  async created() {
    await this.fetchJsonData()
    //array for tables to populate charts base on promotion stats
    this.dataArr = this.convertToDataArray(this.jsonData.promo_stats, 'promo_stats');

    //array for tables to populates based on retailer grouping
    this.brandDataArr = this.convertToDataArray(this.jsonData.retailer, 'retailer');
  },
  mounted() {},
};
</script>