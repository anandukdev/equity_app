<template>
<div> 
  <b-button href="http://127.0.0.1:8000/getCsv/">Download</b-button>
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
        fetch('http://127.0.0.1:8000/getCsv/')
        .then(res => res.json())
        .then(json => {
            this.equities = json;
        });
    },
    
    
}
</script>