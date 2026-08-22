<script>
    import { onMount } from 'svelte';

    let status = $state({
        front_camera_status: null,
        top_camera_status: null,
        short_camera_status: null,
        front_camera_ip: '',
        top_camera_ip: '',
        short_camera_ip: ''
    });

    async function fetchStatus() {
        try {
            const response = await fetch('http://localhost:8000/status');
            status = await response.json();
        } catch (err) {
            console.error('Failed to fetch status:', err);
            status = {
                front_camera_status: null,
                top_camera_status: null,
                short_camera_status: null,
                
                front_camera_ip: '',
                top_camera_ip: '',
                short_camera_ip: ''
            }
        }
    }

    function statusText(code) {
        return code === 200 ? 'Success' : 'Error';
    }

    function statusColor(code) {
        return code === 200 ? 'text-success' : 'text-error';
    }

    onMount(() => {
        fetchStatus();
    });
</script>

<div class="w-full p-2 rounded-box shadow-sm bg-base-200 grid grid-cols-1 sm:grid-cols-3 gap-2">
    <div class="stats stats-vertical">
        <div class="stat">
            <div class="stat-title font-bold">Connectivity: Long View</div>
            <div class={`stat-value capitalize ${statusColor(status.front_camera_status)}`}>
                {statusText(status.front_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address: Long View</div>
            <div class="stat-value capitalize text-2xl">
                {status.front_camera_ip}
            </div>
        </div>
    </div>
    <div class="stats stats-vertical">
        <div class="stat">
            <div class="stat-title font-bold">Connectivity: Top View</div>
            <div class={`stat-value capitalize ${statusColor(status.top_camera_status)}`}>
                {statusText(status.top_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address: Top View</div>
            <div class="stat-value capitalize text-2xl">
                {status.top_camera_ip}
            </div>
        </div>
    </div>
    <div class="stats stats-vertical">
        <div class="stat">
            <div class="stat-title font-bold">Connectivity: Short View</div>
            <div class={`stat-value capitalize ${statusColor(status.short_camera_status)}`}>
                {statusText(status.short_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address: Short View</div>
            <div class="stat-value capitalize text-2xl">
                {status.short_camera_ip}
            </div>
        </div>
    </div>

    <!-- Refresh Button -->
    <button class="btn btn-sm btn-dashed sm:col-span-3" onclick={fetchStatus}>
        Refresh
    </button>
</div>