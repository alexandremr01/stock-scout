<template>
  <div class="card-bg">
    <container class="remove-button">
      <b-button>Remove </b-button>
    </container>
    <container class="chart">
      <vue-apex-charts
        ref=""
        width="100%"
        :type="this.chartType"
        :options="this.chartType === `line` ? lineOptions : candlestickOptions"
        :series="this.chartSeries"
      />
    </container>
    <container class="frequency-options"></container>
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
    };
  },
  components: { VueApexCharts },
  props: ["chartType", "stock", "categories", "chartSeries"],
  created() {
    if (this.chartType == "line") {
      this.lineOptions.xaxis.categories = this.categories;
      this.lineOptions.title.text = this.stock;
    }
    else if (this.chartType == "candlestick") {
      this.candlestickOptions.xaxis.categories = this.categories;
      this.candlestickOptions.title.text = this.stock;
    }
  }
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
  padding: 0;
  box-shadow: 10px 10px 2px 1px rgba(0, 0, 0, 0.2);
  height: 500px;
  width: 500px;
}

.remove-button {
}

.chart {
}

.frequency-options {
}
</style>