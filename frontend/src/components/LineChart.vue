<script>
import VueApexCharts from 'vue-apexcharts'

export default {    
    props: {
        label: {
            type: String
        },
        chart_data: {
            type: Array
        },
        options: {
            type: Object
        }
    },
    mounted() {
        const date = this.chart_data.map(stock_data => stock_data.date).reverse();
        const price = this.chart_data.map(stock_data => stock_data.price).reverse();

        console.log(price);

        var chart = new Vue({
            el: '#appl',
            data: function() {
                return {
                    options: {
                        chart: {
                            id: 'example'
                        },
                        xaxis: {
                            date: date
                        }
                    },
                    series: [{
                        name: 'example',
                        data: price,
                    }]
                }
            }
        })
    }
}
</script>