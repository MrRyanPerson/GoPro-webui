<script lang="ts">
    let previews = $state([])

    async function loadPreview() {
        previews = []
        try {
            const response = await fetch('http://localhost:8000/preview');
            previews = (await response.json())["previews"];
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-xl sm:text-2xl font-bold w-full">Generate Preview</h1>
    <button onclick={()=>{
            loadPreview();
            (document.getElementById('preview_modal') as HTMLDialogElement)?.showModal();
        }} 
        class="btn btn-dash btn-block h-36 my-2">Open Preview</button>
    <dialog id="preview_modal" class="modal">
        <div class="modal-box max-w-7xl w-11/12">
            <div class="grid gap-4 grid-cols-1 sm:grid-cols-3">
                {#if previews.length > 0}
                    {#each previews as preview (preview)}
                        <video
                            class="w-full rounded-lg aspect-video bg-black"
                            src={preview}
                            loop
                            autoplay
                            muted
                            playsinline
                        ></video>
                    {/each}
                {:else}
                    {#each [1,2,3]}
                    <div>
                        <div class="skeleton h-48 w-full flex items-center justify-center">
                            <span class="skeleton skeleton-text">Loading...</span>
                        </div>
                    </div>
                    {/each}
                {/if}
            </div>

            <div class="modal-action">
                <form method="dialog">
                    <button class="btn">Close</button>
                </form>
            </div>
        </div>
    </dialog>
</div>