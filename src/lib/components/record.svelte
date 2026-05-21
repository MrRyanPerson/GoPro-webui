<script lang="ts">
    let status = $state()

    async function record() {
        try {
            if (document.getElementById("experiment_name")?.value !== "") {
                const response = await fetch('http://localhost:8000/start_record',{
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ name: document.getElementById("experiment_name")?.value })
                });
                status = await response.json();
                console.log(status)
            }
            else {
                alert("Please Provide an Experiment Name")
            }
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }

    }
       
    async function stop_record() {
        try {
            if (document.getElementById("experiment_name")?.value !== "") {
                const response = await fetch('http://localhost:8000/stop_record',{
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ name: document.getElementById("experiment_name")?.value })
                });
                status = await response.json();
                console.log(status)
            }
            else {
                alert("Please Provide an Experiment Name")
            }

        } catch (err) {
            console.error('Failed to fetch status:', err);
        }

    }


</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-xl sm:text-2xl font-bold w-full">Record</h1>
    <p class="opacity-60 text-sm mt-2">Experiment name</p>
    <label class="input mt-2 mb-4">
        <svg xmlns="http://www.w3.org/2000/svg" class="size-[1.5em] opacity-50 fill-current" viewBox="0 -960 960 960"><path d="M200-120q-51 0-72.5-45.5T138-250l222-270v-240h-40q-17 0-28.5-11.5T280-800q0-17 11.5-28.5T320-840h320q17 0 28.5 11.5T680-800q0 17-11.5 28.5T640-760h-40v240l222 270q32 39 10.5 84.5T760-120H200Zm80-120h400L544-400H416L280-240Zm-80 40h560L520-492v-268h-80v268L200-200Zm280-280Z"/></svg>
        <input id="experiment_name" type="text" class="grow" placeholder="STJ_AJ_21_vid01" />
    </label>
    <div class="flex">
        <button onclick={record} class="mx-2 btn btn-block size-36 rounded-box bg-success flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="40px" fill="#e3e3e3"><path d="M158.67-242.67q-37-50.66-57.84-110.5Q80-413 80-480t20.33-127q20.34-60 57.34-110l48 47.67q-28 40.66-43.5 88.5Q146.67-533 146.67-480t15.83 101.33q15.83 48.34 43.83 89l-47.66 47ZM480-80q-66.33 0-126.67-20.33Q293-120.67 243-157.67l47.67-48q40.66 28 88.5 43.5Q427-146.67 480-146.67t100.83-15.5q47.84-15.5 88.5-43.5l47.67 48q-50 37-110 57.34Q547-80 480-80Zm322-162-47.67-47.67q28-40.66 43.5-89Q813.33-427 813.33-480t-15.5-100.83q-15.5-47.84-43.5-88.5l48-47.67q37 50 57.34 110Q880-547 880-480t-20.5 127.17Q839-292.67 802-242ZM289.67-754.33 242-802q50.67-37 110.83-57.5Q413-880 480-880q67.33 0 127.33 20.83 60 20.84 110.67 57.84l-47.67 47.66q-40.66-28-88.66-43.83-48-15.83-101.67-15.83-53 0-101.33 15.5-48.34 15.5-89 43.5ZM480-286.67q-80.33 0-136.83-56.5-56.5-56.5-56.5-136.83 0-80.33 56.5-136.83 56.5-56.5 136.83-56.5 80.33 0 136.83 56.5 56.5 56.5 56.5 136.83 0 80.33-56.5 136.83-56.5 56.5-136.83 56.5Z"/></svg>
            <p class="text-[#e3e3e3]">Record</p>
        </button>
        <button onclick={stop_record} class="size-36 btn btn-block rounded-box bg-error">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="40px" fill="#181818"><path d="M158.67-242.67q-37-50.66-57.84-110.5Q80-413 80-480t20.33-127q20.34-60 57.34-110l48 47.67q-28 40.66-43.5 88.5Q146.67-533 146.67-480t15.83 101.33q15.83 48.34 43.83 89l-47.66 47ZM480-80q-66.33 0-126.67-20.33Q293-120.67 243-157.67l47.67-48q40.66 28 88.5 43.5Q427-146.67 480-146.67t100.83-15.5q47.84-15.5 88.5-43.5l47.67 48q-50 37-110 57.34Q547-80 480-80Zm322-162-47.67-47.67q28-40.66 43.5-89Q813.33-427 813.33-480t-15.5-100.83q-15.5-47.84-43.5-88.5l48-47.67q37 50 57.34 110Q880-547 880-480t-20.5 127.17Q839-292.67 802-242ZM289.67-754.33 242-802q50.67-37 110.83-57.5Q413-880 480-880q67.33 0 127.33 20.83 60 20.84 110.67 57.84l-47.67 47.66q-40.66-28-88.66-43.83-48-15.83-101.67-15.83-53 0-101.33 15.5-48.34 15.5-89 43.5ZM480-286.67q-80.33 0-136.83-56.5-56.5-56.5-56.5-136.83 0-80.33 56.5-136.83 56.5-56.5 136.83-56.5 80.33 0 136.83 56.5 56.5 56.5 56.5 136.83 0 80.33-56.5 136.83-56.5 56.5-136.83 56.5Z"/></svg>
            <p class="text-[#181818]">Stop</p>
        </button>
    </div>
</div>