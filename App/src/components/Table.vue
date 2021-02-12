<template>     
        <div class="container">
           <!-- <input class="searchbox" type="text" v-model="search" placeholder="Search Name"> -->
           <b-button class="button-align" href="http://127.0.0.1:8000/getCsv/">Download</b-button> 
            <div class="table-responsive">
                <div class="align">
                <table class="table table-bordered table-striped" id="tracerouteTable">
                    <tr>
                        <th class="align">Code</th>
                        <th>Name</th>
                        <th>Open</th>
                        <th>High</th>
                        <th>Low</th>
                        <th>Close</th>
                    </tr>
                    <tr v-for="data in equities" :key="data.code">
                        <td>{{data.code}}</td>
                        <td>{{data.name}}</td>
                        <td>{{data.open}}</td>
                        <td>{{data.high}}</td>
                        <td>{{data.low}}</td>
                        <td>{{data.close}}</td>
                    </tr>
                    <tr v-if="equities.length === 0">
                        <td colspan="6" class="text-center">Wait for the Records !</td>
                    </tr>
                </table>
                </div>
            </div>
        </div>

</template>

<script>

export default {
    name: 'Table',
    data() {
        return {
            equities: [],
            
        };
    },
    mounted() {
        fetch('http://127.0.0.1:8000/getTradeData/')
        .then(res => res.json())
        .then(json => {
            this.equities = json;
        });
    },
    
}
</script>

<style scoped>
.align {margin-top: 3%;}
.searchbox {width: 100%; margin-top: 2%;}
.button-align {margin-left: 85%; margin-top: 4%;}
</style>