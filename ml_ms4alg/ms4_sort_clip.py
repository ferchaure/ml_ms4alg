import numpy as np
from msalg import branch_cluster, compute_principal_components
def sort_clip(clips, num_features = 10, max_num_clips_for_pca=1000)

    # Subsample and extract clips for pca
    inds=np.random.choice(clisp.shape[0], max_num_clips_for_pca, replace=False)

    # use twice as many features, because of branch method
    principal_components=compute_principal_components(clips[inds,:],num_features*2) # (MT x 2F)

    # Compute the features for all the clips
    features=np.zeros((num_features*2,len(times)))
    features=principal_components.transpose() @ clips # (2F x MT) @ (MT x L0) -> (2F x L0)   
    labels=branch_cluster(features,branch_depth=2,npca=num_features)
return labels