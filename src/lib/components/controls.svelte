<script lang="ts">

    let presets = $state({});
    let zoom = $state(0)

    function openConfirm(){
        (document.getElementById('confirm_modal') as HTMLDialogElement)?.showModal();
    }
    function openZoom(){
        (document.getElementById('zoom_modal') as HTMLDialogElement)?.showModal();
    }
    async function setZoom(){
        zoom = document.getElementById('zoom_slider')?.value
        try {
            await fetch('http://localhost:8000/zoom/' + zoom);
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function openPresets() {
        presets = await getPresets();
        (document.getElementById('preset_modal') as HTMLDialogElement)?.showModal();
    }
    async function clearGopros() {
        try {
            await fetch('http://localhost:8000/controls/clear_gopros');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function setKeepAlive() {
        try {
            await fetch('http://localhost:8000/controls/set_keep_alive');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function resetConnection() {
        try {
            await fetch('http://localhost:8000/controls/reset_connection');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }

    async function getPresets() {
        try {
            let response = await fetch('http://localhost:8000/controls/get_presets');
            response = await response.json()
            response = response["presets"];
            console.log(response);
            return response;
        } catch (err) {
            console.error('Failed to fetch status:', err);
            return;
        }
    }

</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-2xl m-2 font-bold text-content">Extra Controls</h1>
    <div class="grid gap-2 grid-cols-2 sm:grid-cols-3">
        <button class="btn btn-block" onclick={openConfirm}>
            Clear GoPro
        </button>
        <button class="btn btn-block" onclick={setKeepAlive}>
            Keep Alive
        </button>
        <button class="btn btn-block" onclick={openPresets}>
            Get Presets
        </button>
        <button class="btn btn-block" onclick={openZoom}>
            Set Top Zoom
        </button>
        <button class="btn btn-block" onclick={resetConnection}>
            Reset Connection
        </button>

    </div>
</div>

<!-- Dialogs -->

<dialog id="preset_modal" class="modal">
    <div class="modal-box">
        <div class="divider text-lg sm:text-xl font-semibold my-3">Front Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.front_gopro}{presets.front_gopro["resolution"]}{/if}</div>
            </div>
        </div>
                <div class="divider text-lg sm:text-xl font-semibold my-3">Top Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.top_gopro}{presets.top_gopro["resolution"]}{/if}</div>
            </div>
        </div>
        <div class="divider text-lg sm:text-xl font-semibold my-3">Short Gopro</div>
        <div class="stats shadow">
            <div class="stat">
                <div class="stat-title">Recording FPS</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["fps"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Lens Mode</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["lens_mode"]}{/if}</div>
            </div>
            <div class="stat">
                <div class="stat-title">Resolution</div>
                <div class="stat-value text-lg">{#if presets?.short_gopro}{presets.short_gopro["resolution"]}{/if}</div>
            </div>
        </div>

        <form method="dialog" class="m-4">
            <button class="btn">Close</button>
        </form>
    </div>
</dialog>

<dialog id="confirm_modal" class="modal">
    <div class="modal-box">
        <h1 class="text-xl sm:text-2xl font-bold">Clear Gopros?</h1>
        <p class="text-md sm:text-lg">Would you like to clear to GoPros?</p>
        <div class="modal-action">
            <form onsubmit={
                ()=>{
                    clearGopros();
                    (document.getElementById('confirm_modal') as HTMLDialogElement)?.close();
                }
            }>
                <button class="btn btn-block btn-error w-full">Clear</button>
            </form>
            <form method="dialog">
                <button class="btn">Close</button>
            </form>
        </div>
    </div>
</dialog>

<dialog id="zoom_modal" class="modal">
    <div class="modal-box">
        <h1 class="text-lg sm:text-xl font-bold">Set zoom for Top Camera.</h1>
        <form class="m-4 pt-2">
            <div class="w-full max-w-xs">
            <input type="range" min="0" max="100" value="0" class="range range-xl" step="50" id="zoom_slider" onchange={setZoom} />
            <div class="flex justify-between px-2.5 mt-2 text-xs">
                <span>|</span>
                <span>|</span>
                <span>|</span>
            </div>
            <div class="flex justify-between px-2.5 mt-2 text-xs sm:text-sm">
                <span>1.0x</span>
                <span>1.5x</span>
                <span>2.0x</span>
            </div>
            </div>
        </form>
        <div class="modal-action">
            <form method="dialog">
                <button class="btn">Close</button>
            </form>
        </div>
    </div>
</dialog>

