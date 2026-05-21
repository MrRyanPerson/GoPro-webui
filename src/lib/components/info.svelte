<script>
    import { onMount } from 'svelte';

    let status = {
        front_camera_status: null,
        top_camera_status: null,
        short_camera_status: null,
        front_camera_ip: '',
        top_camera_ip: '',
        short_camera_ip: ''
    };

    async function fetchStatus() {
        try {
            const response = await fetch('https://glowing-xylophone-pv6x9jqx6v7hggg-8000.app.github.dev');
            status = await response.json();
        } catch (err) {
            console.error('Failed to fetch status:', err);
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
            <div class="stat-title font-bold">Connectivity for Front Camera</div>
            <div class={`stat-value capitalize ${statusColor(status.front_camera_status)}`}>
                {statusText(status.front_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address for Front Camera</div>
            <div class="stat-value capitalize text-2xl">
                {status.front_camera_ip}
            </div>
        </div>
    </div>
    <div class="stats stats-vertical">
        <div class="stat">
            <div class="stat-title font-bold">Connectivity for Top Camera</div>
            <div class={`stat-value capitalize ${statusColor(status.top_camera_status)}`}>
                {statusText(status.top_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address for Top Camera</div>
            <div class="stat-value capitalize text-2xl">
                {status.top_camera_ip}
            </div>
        </div>
    </div>
    <div class="stats stats-vertical">
        <div class="stat">
            <div class="stat-title font-bold">Connectivity for Short Camera</div>
            <div class={`stat-value capitalize ${statusColor(status.short_camera_status)}`}>
                {statusText(status.short_camera_status)}
            </div>
        </div>

        <div class="stat overflow-hidden text-clip">
            <div class="stat-title font-bold">IP Address for Short Camera</div>
            <div class="stat-value capitalize text-2xl">
                {status.short_camera_ip}
            </div>
        </div>
    </div>

    <!-- Refresh Button -->
    <button class="btn btn-sm btn-dashed sm:col-span-3" on:click={fetchStatus}>
        Refresh
    </button>
</div>