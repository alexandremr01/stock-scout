<template>
  <div class="card-bg">
    <container class="remove-button">
      <b-button pill @click="removeChart">
        <b-icon icon="x-circle-fill"></b-icon>
      </b-button>
    </container>
    <container class="chart">
      <vue-apex-charts
        :type="this.chartType"
        :options="this.chartType === `line` ? lineOptions : candlestickOptions"
        :series="this.chartSeries"
      />
    </container>
    <container class="frequency-options">
      <b-button-group class="frequencyOptions" size="lm">
        <b-button
          v-for="(btn, idx) in frequencyOptions.buttons"
          :key="idx"
          :pressed.sync="btn.state"
          variant="primary"
          @click="frequencyOnPress(idx)"
          class="frequencyOptionsButton"
        >
          <b-icon :icon="btn.icon"></b-icon>&nbsp;{{ btn.caption }}
        </b-button>
      </b-button-group>
    </container>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "graphCard",
  data() {
    return {
      lineOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        colors: ["#358C59"], // @todo
        dataLabels: {
          enabled: false, // todo: add button to enable/disable
          style: {
            fontSize: "12px",
          },
        },
        grid: {
          borderColor: "#2f373c",
        },
        xaxis: {
          categories: [],
          type: "datetime",
          labels: {
            format: "dd MMM",
            style: {
              colors: "#2f373c",
              fontSize: "16px",
            },
          },
        },
        yaxis: {
          decimalsInFloat: 0,
          labels: {
            style: {
              colors: "#2f373c",
              fontSize: "16px",
            },
          },
          title: {
            text: "Price",
            style: {
              color: "#2f373c",
              fontSize: "18px",
            },
          },
        },
        stroke: {
          curve: "smooth",
          width: 3,
        },
        theme: {
          mode: "light",
        },
        title: {
          text: "",
          align: "center",
          offsetY: 10,
          style: {
            fontSize: "18px",
            fontWeight: "bold",
            color: "#2f373c",
          },
        },
        tooltip: {
          custom: function ({ series, seriesIndex, dataPointIndex, w }) {
            return (
              '<div class="arrow_box">' +
              "<span>" +
              series[seriesIndex][dataPointIndex] +
              " USD" +
              "</span>" +
              "</div>"
            );
          },
        },
      },
      candlestickOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        colors: ["#cc5d18"], // @todo
        xaxis: {
          categories: [],
          type: "datetime",
          labels: {
            format: "dd MMM",
            style: {
              colors: "#2f373c",
              fontSize: "16px",
            },
          },
        },
        grid: {
          borderColor: "#2f373c",
        },
        yaxis: {
          decimalsInFloat: 0,
          labels: {
            style: {
              colors: "#2f373c",
              fontSize: "16px",
            },
          },
          title: {
            text: "Price",
            style: {
              color: "#2f373c",
              fontSize: "18px",
            },
          },
        },
        stroke: {
          curve: "smooth",
          width: 3,
        },
        theme: {
          mode: "light",
        },
        title: {
          text: "",
          align: "center",
          offsetY: 10,
          style: {
            fontSize: "18px",
            fontWeight: "bold",
            color: "#2f373c",
          },
        },
      },
      frequencyOptions: {
        buttons: [
          {
            caption: "Daily",
            state: true,
            frequency: "DAY",
            icon: "calendar3-event",
          },
          {
            caption: "Weekly",
            state: false,
            frequency: "WEEK",
            icon: "calendar3-week",
          },
          {
            caption: "Monthly",
            state: false,
            frequency: "MONTH",
            icon: "calendar3",
          },
        ],
      },
    };
  },
  methods: {
    removeChart() {
      console.log(this.id);
      this.$emit("remove", this.id);
    },
    frequencyOnPress(i) {
      this.lineChartFrequencyOptions.buttons.forEach(
        (btn, index) => (btn.state = i === index)
      );
      this.lineChartFrequencyOptions.buttons.forEach((btn, index) =>
        i === index ? this.changeChartFrequency(btn.frequency) : null
      );
      this.lineChartFrequencyOptions.buttons.forEach((btn, index) =>
        i === index ? (this.stockFrequency = btn.frequency) : null
      );
    },
  },
  components: { VueApexCharts },
  props: ["chartType", "stock", "categories", "chartSeries", "id"],
  created() {
    if (this.chartType == "line") {
      this.lineOptions.xaxis.categories = this.categories;
      this.lineOptions.title.text = this.stock;
    } else if (this.chartType == "candlestick") {
      this.candlestickOptions.xaxis.categories = this.categories;
      this.candlestickOptions.title.text = this.stock;
    }
  },
};
</script>

<style>
.card-bg {
  display: flex;
  flex-direction: column;
  background: rgb(234, 243, 243);
  background: linear-gradient(
    to bottom right,
    rgba(234, 243, 243, 1) 0%,
    rgba(203, 214, 208, 1) 35%,
    rgba(190, 205, 206, 1) 100%
  );
  padding: 10px;
  box-shadow: 10px 10px 2px 1px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
}

.remove-button {
  align-self: flex-end;
}

.chart {
  align-self: center;
  width: 100%;
  height: auto;
}

.frequency-options {
}
</style>