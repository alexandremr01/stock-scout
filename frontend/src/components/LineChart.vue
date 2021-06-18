<script>
import {Line} from 'vue-chartjs'

export default {
    extends: Line,
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

        this.renderChart(
        {
            labels: date,
            datasets: [{
                label: this.label,
                chart_data: price,
            }]
        },
        this.options)
    }
}
</script>